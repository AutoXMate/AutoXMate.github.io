---
trust_level: community
id: macos-defense-evasion-mktemp
namespace: macos:defenseevasion:mktemp
name: mktemp
description: Create a temporary file or directory and return the file/directory name to stdout
author: Tim Peck (@B0bby_Tablez)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - defense-evasion
execution:
  template: "mktemp"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Generate payload directory (Shlayer): The following command can be used to generate a random directory name for staging payloads"
    command: "export tmpDir=\"$(mktemp -d /tmp/XXXXXXXXXXXX)\""
  - description: "Generate directory based on template file (Bundlore): The following command can be used to generate a unique directory based on a template"
    command: "TMP_DIR=\"mktemp -d -t x\""
install:
  - method: custom
    commands:
      - "/usr/bin/mktemp"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "Shlayer malware abusing Gatekeeper bypass on macOS"
    url: "https://www.jamf.com/blog/shlayer-malware-abusing-gatekeeper-bypass-on-macos/"
  - label: "20 Common Tools & Techniques Used by macOS Threat Actors & Malware"
    url: "https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/"
---

The mktemp binary located in "usr/bin/mktemp" can generate unique directory or file names and has historically been used to generate unique payloads.