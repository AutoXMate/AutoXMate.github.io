---
id: cmd-csvde
namespace: security:ad:export
name: csvde
description: Imports and exports Active Directory objects using CSV format files.
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
  template: csvde /?
  sandbox: execFile
examples:
- description: Run csvde with default options
  command: csvde /?
references:
- label: csvde Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/csvde
---
