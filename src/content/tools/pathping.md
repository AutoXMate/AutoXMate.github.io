---
id: win-pathping
namespace: network:diagnostic:latency
name: pathping
description: Combines ping and tracert with packet loss per hop.
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
  template: pathping /?
  sandbox: execFile
examples:
- description: Display help for pathping
  command: pathping /?
references:
- label: pathping Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pathping
---
