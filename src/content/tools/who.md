---
id: sys-who
namespace: system:linux:user
name: who
description: Displays who is logged in and their session details.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: who --help
  sandbox: execFile
examples:
- description: Display help for who
  command: who --help
references:
- label: who Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/who
---
