---
id: cmd-gpresult
namespace: system:windows:policy
name: gpresult
description: Displays the Resultant Set of Policy (RSoP) information for a target
  user and computer.
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
  template: gpresult /?
  sandbox: execFile
examples:
- description: Run gpresult with default options
  command: gpresult /?
references:
- label: gpresult Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult
---
