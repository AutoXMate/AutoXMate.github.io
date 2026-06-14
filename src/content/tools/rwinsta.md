---
id: win-rwinsta
namespace: remote:ts:reset
name: rwinsta
description: Resets a Remote Desktop Services session.
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
  template: rwinsta /?
  sandbox: execFile
examples:
- description: Display help for rwinsta
  command: rwinsta /?
references:
- label: rwinsta Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rwinsta
---
