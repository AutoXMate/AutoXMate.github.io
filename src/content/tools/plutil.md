---
trust_level: community
id: macos-defense-evasion-plutil
namespace: macos:defenseevasion:plutil
name: plutil
description: Read, create or edit plist files.
author: Brendan Chamberlain (@infosecB)
version: 1.0.0
capabilities:
- security.defenseevasion.bypass
platforms:
- macos
techniques:
- defense-evasion
execution:
  template: plutil
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Set app to run with dock icon hidden: plutil can be used to set the
    "LSUIElement" attribute to true which will force the targeted app to run without
    the UI and dock icon.'
  command: plutil -insert LSUIElement -string "1" /Applications/TargetApp.app/Contents/Info.plist
install:
- method: custom
  commands:
  - /usr/bin/plutil
detections:
- type: splunk
  url: https://research.splunk.com/endpoint/c11f2b57-92c1-4cd2-b46c-064eafb833ac/
  description: 'Splunk Security Content: MacOS plutil'
references:
- label: Editing Property Lists with plutil
  url: https://scriptingosx.com/2016/11/editing-property-lists/
- label: Plist File Modification (MITRE ATT&CK)
  url: https://attack.mitre.org/techniques/T1647/
features:
- file-system
- local
- pipes-stdout
- stealth
---

plutil is a command-line utility used for managing property list (.plist) files. These files are commonly used by macOS to store a app settings and other configuration info. The utility allows users to check the validity of plist files `plutil -lint`, convert plist files between XML and binary formats (plutil -convert), and add, modify or remove plist key value pairs.
