---
id: sys-lsattr
namespace: system:linux:file
name: lsattr
description: Lists file attributes on ext2/ext3/ext4 filesystems.
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
  template: lsattr --help
  sandbox: execFile
examples:
- description: Display help for lsattr
  command: lsattr --help
references:
- label: lsattr Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsattr
---
