---
id: cmd-diskpart
namespace: system:windows:disk
name: diskpart
description: Command-line disk partitioning utility for managing disks, partitions,
  volumes, and virtual hard disks.
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
  template: diskpart /?
  sandbox: execFile
examples:
- description: Run diskpart with default options
  command: diskpart /?
references:
- label: diskpart Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart
---
