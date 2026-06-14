---
id: sys-depmod
namespace: system:linux:kernel
name: depmod
description: Generates modules.dep and map files for kernel modules.
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
  template: depmod --help
  sandbox: execFile
examples:
- description: Display help for depmod
  command: depmod --help
references:
- label: depmod Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/depmod
---
