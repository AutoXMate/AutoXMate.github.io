---
id: win-reagentc
namespace: system:windows:recovery
name: reagentc
description: Windows Recovery Environment configuration tool.
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
  template: reagentc /?
  sandbox: execFile
examples:
- description: Display help for reagentc
  command: reagentc /?
references:
- label: reagentc Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reagentc
---
