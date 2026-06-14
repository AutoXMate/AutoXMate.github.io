---
id: sys-lspci
namespace: system:linux:pci
name: lspci
description: Lists all PCI devices connected to the system.
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
  template: lspci --help
  sandbox: execFile
examples:
- description: Display help for lspci
  command: lspci --help
references:
- label: lspci Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lspci
---
