---
id: sys-mountpoint
namespace: system:linux:filesystem
name: mountpoint
description: Checks if a directory is a mount point.
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
  template: mountpoint --help
  sandbox: execFile
examples:
- description: Display help for mountpoint
  command: mountpoint --help
references:
- label: mountpoint Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mountpoint
---
