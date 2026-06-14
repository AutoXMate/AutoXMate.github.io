---
id: win-tsdiscon
namespace: remote:ts:disconnect
name: tsdiscon
description: Disconnects a Remote Desktop Services session.
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
  template: tsdiscon /?
  sandbox: execFile
examples:
- description: Display help for tsdiscon
  command: tsdiscon /?
references:
- label: tsdiscon Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tsdiscon
---
