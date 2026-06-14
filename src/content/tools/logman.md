---
id: cmd-logman
namespace: system:windows:monitor
name: logman
description: Manages Performance Monitor logs and traces for data collector sets.
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
  template: logman /?
  sandbox: execFile
examples:
- description: Run logman with default options
  command: logman /?
references:
- label: logman Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman
---
