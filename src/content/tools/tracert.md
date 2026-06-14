---
id: win-tracert
namespace: network:diagnostic:trace
name: tracert
description: Traces the route packets take to a network destination.
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
- T1046
parameters: []
execution:
  template: tracert /?
  sandbox: execFile
examples:
- description: Display help for tracert
  command: tracert /?
references:
- label: tracert Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert
---
