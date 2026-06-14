---
id: winver
namespace: system:windows:info
name: winver
description: Displays a dialog box showing the current Windows version, build number, and system information.
version: "1.0.0"
capabilities:
  - windows-command
  - system-administration
  - information-gathering
features:
  - local
  - batch
install:
  - method: native
    commands:
      - ""
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        winver
  background_templates: []
examples:
  - cmd: "winver /?"
    description: "Display help and usage information for winver"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winver
---