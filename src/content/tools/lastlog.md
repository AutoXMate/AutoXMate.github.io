---
id: sys-lastlog
namespace: system:linux:auth
name: lastlog
description: Reports the most recent login of all users or a given user.
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
  template: lastlog --help
  sandbox: execFile
examples:
- description: Display help for lastlog
  command: lastlog --help
references:
- label: lastlog Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lastlog
---
