---
id: cmd-bcdedit
namespace: system:windows:boot
name: bcdedit
description: Boot Configuration Data editor for managing boot configuration and troubleshooting
  startup issues.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids: []
parameters: []
execution:
  template: bcdedit /?
  sandbox: execFile
examples:
- description: Run bcdedit with default options
  command: bcdedit /?
references:
- label: bcdedit Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit
---
