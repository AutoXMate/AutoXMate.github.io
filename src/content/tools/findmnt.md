---
id: sys-findmnt
namespace: system:linux:filesystem
name: findmnt
description: Lists all currently mounted filesystems in a tree format.
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
  template: findmnt --help
  sandbox: execFile
examples:
- description: Display help for findmnt
  command: findmnt --help
references:
- label: findmnt Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/findmnt
---
