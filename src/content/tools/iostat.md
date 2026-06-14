---
id: sys-iostat
namespace: system:linux:monitor
name: iostat
description: Reports CPU and I/O statistics for devices and partitions.
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
  template: iostat --help
  sandbox: execFile
examples:
- description: Display help for iostat
  command: iostat --help
references:
- label: iostat Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/iostat
---
