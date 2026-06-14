---
id: sys-modinfo
namespace: system:linux:kernel
name: modinfo
description: Displays information about a kernel module.
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
  template: modinfo --help
  sandbox: execFile
examples:
- description: Display help for modinfo
  command: modinfo --help
references:
- label: modinfo Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/modinfo
---
