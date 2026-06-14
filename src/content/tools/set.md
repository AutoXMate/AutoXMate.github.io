---
id: cmd-set
namespace: system:windows:cmd
name: set
description: Displays, sets, or removes environment variables. Used without parameters,
  displays all current environment variables.
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
  template: set /?
  sandbox: execFile
examples:
- description: Run set with default options
  command: set /?
references:
- label: set Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set
---
