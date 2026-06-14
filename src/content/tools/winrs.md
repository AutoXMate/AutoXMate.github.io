---
id: winrs
namespace: remote:winrm
name: winrs
description: Windows Remote Shell allows running commands on remote Windows machines via WinRM protocol.
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
        winrs
  background_templates: []
examples:
  - cmd: "winrs /?"
    description: "Display help and usage information for winrs"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winrs
---