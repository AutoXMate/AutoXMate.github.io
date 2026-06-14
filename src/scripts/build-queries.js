/**
 * Build the queries.json index for the structured query system.
 * Reads commands.json and action-taxonomy.json, then generates:
 *   - actions → tools mapping
 *   - tool metadata index
 *   - query presets from tool examples
 *   - keyword patterns for free-text parsing
 */

import fs from "node:fs";
import path from "node:path";

const API_DIR = path.resolve("api/v1");
const PUBLIC_API_DIR = path.resolve("public/api/v1");
const TAXONOMY_PATH = path.resolve("data/action-taxonomy.json");

function loadJSON(filePath) {
  if (!fs.existsSync(filePath)) {
    console.warn(`  WARN: ${filePath} not found, skipping`);
    return null;
  }
  return JSON.parse(fs.readFileSync(filePath, "utf-8"));
}

function domainName(namespace) {
  if (!namespace) return "unknown";
  const idx = namespace.indexOf(":");
  return idx > 0 ? namespace.slice(0, idx) : namespace;
}

function capabilityMatchesAction(cap, actionDef) {
  const patterns = actionDef.capabilities || [];
  for (const p of patterns) {
    // Exact match
    if (cap === p) return true;
    // Prefix segment match — e.g., "network.scan" matches "network.scan.port" but NOT "network.scanner"
    const prefix = p + ".";
    if (cap.startsWith(prefix)) return true;
    // Capability starts with pattern
    if (p.startsWith(cap + ".")) return true;
  }
  return false;
}

function inferActionName(capability, curatedActions) {
  const name = capability
    .replace(/\./g, "-")
    .replace(/[^a-z0-9-]/g, "")
    .toLowerCase();
  // Avoid collision with curated action names
  if (curatedActions.has(name)) {
    return "auto-" + name;
  }
  return name;
}

function buildQueriesIndex(commands, taxonomy) {
  if (!commands || !taxonomy) {
    return { actions: {}, tools: {}, presets: [], keywords: {} };
  }

  const toolMap = {};
  const actionTools = {};
  const domainTools = {};
  const keywordMap = {};
  const presets = [];
  const curatedActionSet = new Set(Object.keys(taxonomy));

  // Initialize action indices
  for (const [actionName, actionDef] of Object.entries(taxonomy)) {
    actionTools[actionName] = {
      default_flags: actionDef.default_flags || "",
      default_target_param: actionDef.default_target_param || "target",
      tool_defaults: actionDef.tool_defaults || {},
      tools: [],
    };
    if (actionDef.keywords) {
      for (const kw of actionDef.keywords) {
        if (!keywordMap[kw]) keywordMap[kw] = [];
        keywordMap[kw].push(actionName);
      }
    }
  }

  for (const cmd of commands) {
    const id = cmd.id || cmd.name || "unknown";
    const name = cmd.name || "unknown";
    const ns = cmd.namespace || "unknown";
    const domain = domainName(ns);

    // Build tool metadata index
    toolMap[id] = {
      id,
      name,
      namespace: ns,
      domain,
      description: cmd.description || "",
      capabilities: cmd.capabilities || [],
      phase: cmd.phase || "",
      techniques: cmd.techniques || [],
      risk_level: cmd.risk_level || "",
      services: cmd.services || [],
      platforms: cmd.platforms || [],
      mitre_ids: cmd.mitre_ids || [],
      execution_template: cmd.execution ? cmd.execution.template : "",
      parameters: (cmd.parameters || []).map((p) => ({
        name: p.name,
        template_key: p.template_key || p.name,
        type: p.type,
        required: p.required,
        default_value: p.default_value,
        aliases: p.aliases || [],
        enum: p.enum || [],
      })),
    };

    // Domain index
    if (!domainTools[domain]) domainTools[domain] = [];
    if (!domainTools[domain].includes(id)) {
      domainTools[domain].push(id);
    }

    // Match tool to curated actions
    const caps = cmd.capabilities || [];
    const matchedActions = new Set();

    for (const cap of caps) {
      for (const [actionName, actionDef] of Object.entries(taxonomy)) {
        if (capabilityMatchesAction(cap, actionDef)) {
          if (!matchedActions.has(actionName)) {
            matchedActions.add(actionName);
            actionTools[actionName].tools.push({
              tool_id: id,
              tool_name: name,
              capability: cap,
              confidence: actionDef.capabilities.includes(cap) ? "exact" : "partial",
            });
          }
        }
      }
    }

    // Auto-generate inferred actions for unmatched capabilities
    for (const cap of caps) {
      let matched = false;
      for (const [, actionDef] of Object.entries(taxonomy)) {
        if (capabilityMatchesAction(cap, actionDef)) {
          matched = true;
          break;
        }
      }
      if (!matched) {
        const inferredName = inferActionName(cap, curatedActionSet);
        if (!actionTools[inferredName]) {
          actionTools[inferredName] = {
            default_flags: "",
            default_target_param: "target",
            tool_defaults: {},
            tools: [],
          };
        }
        const exists = actionTools[inferredName].tools.some(
          (e) => e.tool_id === id,
        );
        if (!exists) {
          actionTools[inferredName].tools.push({
            tool_id: id,
            tool_name: name,
            capability: cap,
            confidence: "inferred",
          });
        }
      }
    }

    // Generate presets from tool examples
    const examples = cmd.examples || [];
    let exampleIdx = 0;
    for (const ex of examples) {
      const description = ex.description || ex.label || "";
      const command = ex.command || "";

      // Try to extract a structured query from the example
      const matchedAction = [...matchedActions][0] || "";
      const queryParts = [];
      if (domain) queryParts.push(`domain(${domain})`);
      if (matchedAction) queryParts.push(`action(${matchedAction})`);
      queryParts.push(`tool(${name.toLowerCase().split(" ")[0]})`);
      if (command) {
        // Extract flags
        const flagMatch = command.match(/ -\w+(?: \S+)?/g);
        if (flagMatch) {
          const flags = flagMatch.map((f) => f.trim()).join(" ");
          queryParts.push(`flags(${flags})`);
        }
      }

      presets.push({
        query: queryParts.join(":"),
        command,
        description,
        tool_id: id,
        tool_name: name,
      });

      exampleIdx++;
      if (exampleIdx >= 3) break; // Limit to 3 presets per tool
    }
  }

  return {
    actions: actionTools,
    domains: domainTools,
    tools: toolMap,
    presets,
    keywords: keywordMap,
    curated_actions: Object.keys(taxonomy),
  };
}

function buildQueries() {
  console.log("Building queries index...");

  const taxonomy = loadJSON(TAXONOMY_PATH);
  if (!taxonomy) {
    console.log("  No action-taxonomy.json found, skipping queries index");
    return;
  }

  // Load commands from the primary API dir
  const commandsPath = path.join(API_DIR, "commands.json");
  const commands = loadJSON(commandsPath);
  if (!commands) {
    console.log("  No commands.json found, skipping queries index");
    return;
  }

  const index = buildQueriesIndex(commands, taxonomy);

  console.log(
    `  Indexed ${Object.keys(index.tools).length} tools across ` +
    `${Object.keys(index.actions).length} actions ` +
    `(${Object.keys(index.domains).length} domains) ` +
    `with ${index.presets.length} query presets`,
  );

  const json = JSON.stringify(index, null, 2);

  for (const dir of [PUBLIC_API_DIR, API_DIR]) {
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, "queries.json"), json);
  }

  console.log("  Wrote queries.json to api/v1/ and public/api/v1/");
}

buildQueries();
