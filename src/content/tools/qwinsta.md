---
id: win-qwinsta
namespace: remote:ts:query
name: qwinsta
description: Displays Remote Desktop Services sessions on a server.
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
  template: qwinsta /?
  sandbox: execFile
examples:
- description: Display help for qwinsta
  command: qwinsta /?
references:
- label: qwinsta Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/qwinsta
---
