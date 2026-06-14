---
id: win-recdisc
namespace: system:windows:recovery
name: recdisc
description: Creates a system repair disc.
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
  template: recdisc /?
  sandbox: execFile
examples:
- description: Display help for recdisc
  command: recdisc /?
references:
- label: recdisc Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/recdisc
---
