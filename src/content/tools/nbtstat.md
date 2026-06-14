---
id: win-nbtstat
namespace: network:netbios:stats
name: nbtstat
description: Displays NetBIOS over TCP/IP statistics and name tables.
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
  template: nbtstat /?
  sandbox: execFile
examples:
- description: Display help for nbtstat
  command: nbtstat /?
references:
- label: nbtstat Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nbtstat
---
