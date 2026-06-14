---
id: sys-locale
namespace: system:linux:config
name: locale
description: Displays locale-related environment variables and settings.
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
  template: locale --help
  sandbox: execFile
examples:
- description: Display help for locale
  command: locale --help
references:
- label: locale Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/locale
---
