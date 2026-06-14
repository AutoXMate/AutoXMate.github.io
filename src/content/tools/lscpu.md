---
id: sys-lscpu
namespace: system:linux:cpu
name: lscpu
description: Displays CPU architecture information like cores, threads, model, and
  flags.
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
  template: lscpu --help
  sandbox: execFile
examples:
- description: Display help for lscpu
  command: lscpu --help
references:
- label: lscpu Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lscpu
---
