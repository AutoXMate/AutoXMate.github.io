---
id: net-netstat
namespace: network:monitoring:connections
name: netstat
description: Displays active connections, listening ports, and routing tables.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
- windows
features:
- local
mitre_ids:
- T1049
parameters: []
execution:
  template: netstat
  sandbox: execFile
examples:
- description: Display active network connections
  command: netstat
references:
- label: netstat Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat
- label: netstat manual
  url: https://man7.org/linux/man-pages/man8/netstat.8.html
---
