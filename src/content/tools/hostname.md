---
id: cmd-hostname
namespace: system:windows:cmd
name: hostname
description: Displays the host name portion of the full computer name of the computer.
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
  template: hostname /?
  sandbox: execFile
examples:
- description: Run hostname with default options
  command: hostname /?
references:
- label: hostname Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/hostname
---
