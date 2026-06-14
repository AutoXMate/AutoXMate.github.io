---
trust_level: community
id: macos-credential-access-pbpaste
namespace: macos:credentialaccess:pbpaste
name: pbpaste
description: Paste the contents of clipboard to the terminal.
author: Brendan Chamberlain (@infosecB)
version: "1.0.0"
capabilities:
  - credential.dump
  - collection.data
platforms:
  - macos
techniques:
  - credential-access
  - collection
execution:
  template: "pbpaste"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Use pbpaste to collect sensitive clipboard data: A pbpaste bash loop can continuously collect clipboard contents every x minutes and write contents to a file (or another location). This may allow an attacker to gather user credentials or collect other sensitive information."
    command: "while true; do echo $(pbpaste) >> loot.txt; sleep 10; done"
install:
  - method: custom
    commands:
      - "/usr/bin/pbpaste"
detections:
  - type: sigma
    url: "https://github.com/SigmaHQ/sigma/blob/master/rules-threat-hunting/macos/process_creation/proc_creation_macos_pbpaste_execution.yml"
    description: "Sigma: Clipboard Data Collection Via Pbpaste"
references:
  - label: "Hacking macOS: How to Dump 1Password, KeePassX & LastPass Passwords in Plaintext"
    url: "https://medium.com/@NullByteWht/hacking-macos-how-to-dump-1password-keepassx-lastpass-passwords-in-plaintext-723c5b1c311b"
  - label: "Living-off-the-Land: Exploring macOS LOOBins and Crafting Detection Rules - pbpaste"
    url: "https://danielcortez.substack.com/p/living-off-the-land-exploring-macos-b65"
---

Retrieves the contents of the clipboard (a.k.a. pasteboard) and writes them to the standard output (stdout). The utility is often used for creating new files with the clipboard content or for piping clipboard contents to other commands. It can also be used in shell scripts that may require clipboard content as input.