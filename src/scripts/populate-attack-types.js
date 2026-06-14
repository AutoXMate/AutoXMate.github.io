import fs from "node:fs";
import path from "node:path";
import { glob } from "node:fs/promises";

const TOOLS_DIR = path.resolve("src/content/tools");

const TECHNIQUE_TO_ATTACK_TYPE = {
  "enumeration": "Enumeration",
  "exploitation": "Exploitation",
  "persistence": "Persistence",
  "privilege-escalation": "PrivilegeEscalation",
  "defense-evasion": "DefenseEvasion",
  "credential-access": "CredentialAccess",
  "discovery": "Discovery",
  "lateral-movement": "LateralMovement",
  "collection": "Collection",
  "exfiltration": "Exfiltration",
  "execution": "Execution",
};

async function populateAttackTypes() {
  let updated = 0;
  let skippedExisting = 0;
  let skippedNoTechniques = 0;
  let skippedNoMapping = 0;
  let totalFiles = 0;

  for await (const entry of glob("*.md", { cwd: TOOLS_DIR, root: TOOLS_DIR })) {
    totalFiles++;
    const fullPath = path.join(TOOLS_DIR, entry);
    const raw = fs.readFileSync(fullPath, "utf-8");

    const fmMatch = raw.match(/^---\n([\s\S]*?)\n---\n/);
    if (!fmMatch) {
      console.log(`  SKIP ${entry}: no frontmatter`);
      continue;
    }

    const fmStr = fmMatch[1];
    const body = raw.slice(fmMatch[0].length);

    // Check if attack_types already in frontmatter
    if (/^attack_types:/m.test(fmStr)) {
      skippedExisting++;
      continue;
    }

    // Parse just enough to get techniques (handles both `- item` and `  - item` styles)
    const techniquesMatch = fmStr.match(/^techniques:\n((?:(?:  )?- .+(?:\n|$))*)/m);
    if (!techniquesMatch) {
      skippedNoTechniques++;
      continue;
    }

    const techniquesBlock = techniquesMatch[1];
    const techniques = techniquesBlock
      .split("\n")
      .map(l => l.trim().replace(/^- /, "").replace(/^['"]|['"]$/g, ""))
      .filter(Boolean);

    if (techniques.length === 0) {
      skippedNoTechniques++;
      continue;
    }

    const mapped = techniques
      .map(t => TECHNIQUE_TO_ATTACK_TYPE[t])
      .filter(Boolean);

    if (mapped.length === 0) {
      skippedNoMapping++;
      continue;
    }

    const unique = [...new Set(mapped)].sort();
    const attackTypesYaml = "attack_types:\n" + unique.map(t => `- ${t}`).join("\n") + "\n";

    // Find the end of the techniques block and insert attack_types after it
    const techniquesEnd = fmStr.indexOf(techniquesMatch[0]) + techniquesMatch[0].length;
    const newFmStr = fmStr.slice(0, techniquesEnd) + "\n" + attackTypesYaml + fmStr.slice(techniquesEnd);

    const newContent = "---\n" + newFmStr + "\n---\n" + body;

    fs.writeFileSync(fullPath, newContent, "utf-8");
    updated++;
    console.log(`  OK   ${entry} → [${unique.join(", ")}]`);
  }

  console.log(`\nDone. ${totalFiles} files scanned.`);
  console.log(`  Updated:     ${updated}`);
  console.log(`  Skipped (already had attack_types): ${skippedExisting}`);
  console.log(`  Skipped (no techniques field):      ${skippedNoTechniques}`);
  console.log(`  Skipped (no mapping found):          ${skippedNoMapping}`);
}

populateAttackTypes().catch((err) => {
  console.error("Failed:", err);
  process.exit(1);
});
