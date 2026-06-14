---
id: sys-lsmod
namespace: system:linux:kernel
name: lsmod
description: Lists loaded kernel modules.
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
  template: lsmod --help
  sandbox: execFile
examples:
- description: Display help for lsmod
  command: lsmod --help
references:
- label: lsmod Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsmod
---
