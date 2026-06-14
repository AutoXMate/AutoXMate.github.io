---
id: sys-nproc
namespace: system:linux:cpu
name: nproc
description: Prints the number of processing units available.
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
  template: nproc --help
  sandbox: execFile
examples:
- description: Display help for nproc
  command: nproc --help
references:
- label: nproc Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nproc
---
