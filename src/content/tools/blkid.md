---
id: sys-blkid
namespace: system:linux:disk
name: blkid
description: Locates/prints block device attributes like UUID and filesystem type.
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
  template: blkid --help
  sandbox: execFile
examples:
- description: Display help for blkid
  command: blkid --help
references:
- label: blkid Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/blkid
---
