---
id: win-bootcfg
namespace: system:windows:boot
name: bootcfg
description: Configures Boot.ini for multi-boot systems.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids: []
parameters: []
execution:
  template: bootcfg /?
  sandbox: execFile
examples:
- description: Display help for bootcfg
  command: bootcfg /?
references:
- label: bootcfg Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bootcfg
---
