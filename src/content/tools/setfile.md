---
trust_level: community
id: macos-persistence-setfile
namespace: macos:persistence:setfile
name: SetFile
description: Set attributes of files and directories.
author: Chris Campbell (@texasbe2trill)
version: "1.0.0"
capabilities:
  - security.persistence.hook
  - security.defenseevasion.bypass
platforms:
  - macos
techniques:
  - persistence
  - defense-evasion
execution:
  template: "SetFile"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Set a file or directory attribute to invisible: A bash or zsh oneliner can allow an attacker to set the file attribute to invisible. This action can establish persistence and evade detection for malicious files on the system."
    command: "for FILE in ~/*; do echo $(SetFile -a V $FILE && echo $(GetFileInfo $FILE)) >> /tmp/fileinfo.txt; sleep 2; done"
  - description: "Change a file's creation and modification timestamps: Setfile can be used with the -d and -m arguments to alter a file's creation and modification date, respectively."
    command: "SetFile -d \"04/25/2023 11:11:00\" -m \"04/25/2023 11:12:00\" targetfile.txt"
install:
  - method: custom
    commands:
      - "/usr/bin/SetFile"
detections:
  - type: other
    description: "No detections at time of publishing"
references:
  - label: "The Invisible Bit"
    url: "https://daringfireball.net/2008/04/the_invisible_bit"
---

Uses the CommandLine/Terminal to set file and or directory attributes. It can set attributes, creator, creation date, modification date, and file type for multiple files at a time.