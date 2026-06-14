---
id: sys-eject
namespace: system:linux:device
name: eject
description: Ejects removable media (CD-ROM, USB, etc.) from the system.
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
  template: eject --help
  sandbox: execFile
examples:
- description: Display help for eject
  command: eject --help
references:
- label: eject Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/eject
---
