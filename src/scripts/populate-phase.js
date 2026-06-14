import fs from "node:fs";
import path from "node:path";
import { glob } from "node:fs/promises";

const TOOLS_DIR = path.resolve("src/content/tools");

const TECHNIQUE_TO_PHASE = {
  "recon": "recon",
  "enumeration": "enumeration",
  "exfiltration": "exfiltration",
  "lateral-movement": "lateral-movement",
  "defense-evasion": "defense-evasion",
  "discovery": "discovery",
  "collection": "collection",
  "forensics": "forensics",
  "privilege-escalation": "exploitation",
  "execution": "exploitation",
  "credential-access": "exploitation",
  "impact": "exploitation",
  "persistence": "post-exploitation",
  "command-and-control": "post-exploitation",
  "data-manipulation": "post-exploitation",
  "monitoring": "post-exploitation",
  "backup": "post-exploitation",
  "analysis": "post-exploitation",
  "network-manipulation": "post-exploitation",
  "process-discovery": "post-exploitation",
  "process-termination": "post-exploitation",
  "network-sniffing": "post-exploitation",
  "remote-services": "post-exploitation",
  "encryption": "post-exploitation",
  "process-manip": "post-exploitation",
};

async function populatePhase() {
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

    // Skip if phase already set
    if (/^phase:/m.test(fmStr)) {
      skippedExisting++;
      continue;
    }

    // Parse techniques block (handles both `- item` and `  - item` styles)
    const techniquesMatch = fmStr.match(/^techniques:\n((?:(?:  )?- .+(?:\n|$))*)/m);
    if (!techniquesMatch) {
      skippedNoTechniques++;
      continue;
    }

    const techniquesLines = techniquesMatch[1]
      .split("\n")
      .map(l => l.trim().replace(/^- /, "").replace(/^['"]|['"]$/g, ""))
      .filter(Boolean);

    if (techniquesLines.length === 0) {
      skippedNoTechniques++;
      continue;
    }

    // Find the first technique that maps to a phase
    const phaseVal = techniquesLines
      .map(t => TECHNIQUE_TO_PHASE[t])
      .filter(Boolean)[0];

    if (!phaseVal) {
      skippedNoMapping++;
      continue;
    }

    // Insert phase right after the techniques block
    const block = techniquesMatch[0];
    const blockEnd = fmStr.indexOf(block) + block.length;
    const phaseLine = `phase: ${phaseVal}`;
    const newFmStr = fmStr.slice(0, blockEnd) + phaseLine + "\n" + fmStr.slice(blockEnd);

    const newContent = "---\n" + newFmStr + "\n---\n" + raw.slice(fmMatch[0].length);

    fs.writeFileSync(fullPath, newContent, "utf-8");
    updated++;
    console.log(`  OK   ${entry} → ${phaseVal}`);
  }

  console.log(`\nDone. ${totalFiles} files scanned.`);
  console.log(`  Updated:     ${updated}`);
  console.log(`  Skipped (already had phase):   ${skippedExisting}`);
  console.log(`  Skipped (no techniques field):  ${skippedNoTechniques}`);
  console.log(`  Skipped (no mapping found):     ${skippedNoMapping}`);
}

populatePhase().catch((err) => {
  console.error("Failed:", err);
  process.exit(1);
});
