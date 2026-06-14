---
id: cmd-where
namespace: system:windows:file
name: where
description: Displays the location of files that match the search pattern, similar
  to Unix 'which' but with broader search capabilities.
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
  template: where /?
  sandbox: execFile
examples:
- description: Run where with default options
  command: where /?
references:
- label: where Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where
---
