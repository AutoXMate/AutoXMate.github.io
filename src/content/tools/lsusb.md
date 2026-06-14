---
id: sys-lsusb
namespace: system:linux:usb
name: lsusb
description: Lists USB buses and connected USB devices.
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
  template: lsusb --help
  sandbox: execFile
examples:
- description: Display help for lsusb
  command: lsusb --help
references:
- label: lsusb Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsusb
---
