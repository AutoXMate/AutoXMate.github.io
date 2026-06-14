---
id: sys-lsblk
namespace: system:linux:disk
name: lsblk
description: Lists block devices (disks and partitions) in a tree-like format.
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
  template: lsblk --help
  sandbox: execFile
examples:
- description: Display help for lsblk
  command: lsblk --help
references:
- label: lsblk Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsblk
---
