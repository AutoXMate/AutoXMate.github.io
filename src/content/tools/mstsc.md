---
id: win-mstsc
namespace: remote:rdp:client
name: mstsc
description: Remote Desktop Connection client.
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
  template: mstsc /?
  sandbox: execFile
examples:
- description: Display help for mstsc
  command: mstsc /?
references:
- label: mstsc Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc
---
