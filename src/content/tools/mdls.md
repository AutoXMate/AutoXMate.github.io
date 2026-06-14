---
trust_level: community
id: macos-defense-evasion-mdls
namespace: macos:defenseevasion:mdls
name: mdls
description: List metadata attributes for the specified file.
author: Daniel Stinson-Diess (@shellcromancer)
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
  - discovery.enumerate
  - security.execution.command
  - collection.data
platforms:
  - macos
techniques:
  - defense-evasion
  - discovery
  - execution
  - collection
execution:
  template: "mdls"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Validate file download information: Use mdls to validate payload download sources and timestamps to guard against sandbox executions."
    command: "mdls -name \"kMDItemWhereFroms\" -name \"kMDItemDownloadedDate\""
  - description: "Query File Paths: Use mdls to print file paths and sizes when enumerating host resources."
    command: "xargs -0 mdls -n kMDItemPath -n kMDItemFSSize"
  - description: "Extract and execute payload stored in Finder comment metadata: Every file on macOS has a Finder comment field stored as Spotlight metadata under the kMDItemFinderComment attribute. mdls can read this field and pipe its contents to a decoder and executor. Because the payload lives entirely in Spotlight metadata rather than file contents, it is not visible to file-based inspection or integrity monitoring tools. Finder comments can be written remotely via osascript over Remote Apple Events or SSH, making this a covert staging mechanism for lateral movement payloads."
    command: "mdls -name kMDItemFinderComment -raw ~/Desktop/payload_carrier.txt | base64 -D | bash"
install:
  - method: custom
    commands:
      - "/usr/bin/mdls"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "Bad Apples: Weaponizing Native macOS Primitives for Movement and Execution"
    url: "https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/"
---

mdls list file metadata across standard metadata (creation date, size), extended attribute (quarantine), and Spotlight APIs (Finder flags).