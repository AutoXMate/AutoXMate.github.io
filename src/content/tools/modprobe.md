---
id: sys-modprobe
namespace: system:linux:kernel
name: modprobe
description: Adds or removes kernel modules from the Linux kernel.
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
  template: modprobe --help
  sandbox: execFile
examples:
- description: Display help for modprobe
  command: modprobe --help
references:
- label: modprobe Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/modprobe
---
