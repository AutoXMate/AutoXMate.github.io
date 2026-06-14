---
id: sys-vmstat
namespace: system:linux:monitor
name: vmstat
description: Reports virtual memory statistics, processes, CPU, and I/O activity.
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
  template: vmstat --help
  sandbox: execFile
examples:
- description: Display help for vmstat
  command: vmstat --help
references:
- label: vmstat Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vmstat
---
