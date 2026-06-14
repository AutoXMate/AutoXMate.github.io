---
id: win-tscon
namespace: remote:ts:connect
name: tscon
description: Connects a Remote Desktop session to a different session.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids:
- T1563
parameters: []
execution:
  template: tscon /?
  sandbox: execFile
examples:
- description: Display help for tscon
  command: tscon /?
references:
- label: tscon Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tscon
---
