---
id: win-typeperf
namespace: system:windows:performance
name: typeperf
description: Writes performance counter data to command line or log.
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
  template: typeperf /?
  sandbox: execFile
examples:
- description: Display help for typeperf
  command: typeperf /?
references:
- label: typeperf Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/typeperf
---
