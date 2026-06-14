---
id: cmd-dsquery
namespace: security:ad:query
name: dsquery
description: Active Directory query tool for retrieving objects from the directory.
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
  template: dsquery /?
  sandbox: execFile
examples:
- description: Run dsquery with default options
  command: dsquery /?
references:
- label: dsquery Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dsquery
---
