---
id: sys-uptime
namespace: system:linux:info
name: uptime
description: Shows how long the system has been running, user count, and load averages.
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
  template: uptime --help
  sandbox: execFile
examples:
- description: Display help for uptime
  command: uptime --help
references:
- label: uptime Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/uptime
---
