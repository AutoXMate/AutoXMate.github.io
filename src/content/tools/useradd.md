---
id: sys-useradd
namespace: system:linux:user
name: useradd
description: Creates a new user account with home directory, shell, and groups.
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
  template: useradd --help
  sandbox: execFile
examples:
- description: Display help for useradd
  command: useradd --help
references:
- label: useradd Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/useradd
---
