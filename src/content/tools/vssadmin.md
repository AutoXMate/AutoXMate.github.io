---
id: cmd-vssadmin
namespace: system:windows:backup
name: vssadmin
description: Volume Shadow Copy Service administration tool for managing shadow copies,
  providers, and volumes.
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
  template: vssadmin /?
  sandbox: execFile
examples:
- description: Run vssadmin with default options
  command: vssadmin /?
references:
- label: vssadmin Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/vssadmin
---
