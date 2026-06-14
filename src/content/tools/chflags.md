---
trust_level: community
id: macos-defense-evasion-chflags
namespace: macos:defenseevasion:chflags
name: chflags
description: Changes file or directory flags
author: demonduck
version: "1.0.0"
capabilities:
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - defense-evasion
execution:
  template: "chflags"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Hide a file: Add the hidden flag to a file or directory to prevent it from being \nvisible in Finder and Terminal."
    command: "chflags hidden ~/evil"
  - description: "Remove hidden flag: Remove the hidden flag to a file or directory to make it visible in Finder\nand Terminal."
    command: "chflags nohidden ~/evil"
install:
  - method: custom
    commands:
      - "/usr/bin/chflags"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_chflags_hidden_flag.yml"
    description: "Sigma: Hidden Flag Set On File/Directory Via Chflags"
references:
  - label: "chflags man page"
    url: "https://ss64.com/mac/chflags.html"
  - label: "macOS/binaries/chflags"
    url: "https://macosbin.com/bin/chflags"
  - label: "How to hide files and folders"
    url: "https://eclecticlight.co/2024/07/03/how-to-hide-files-and-folders/"
---

The chflags utility modifies the file flags of the listed files as 
specified by the flags operand.