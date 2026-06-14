---
id: cmd-driverquery
namespace: system:windows:driver
name: driverquery
description: Displays a list of all installed device drivers and their properties
  including driver name, type, and module name.
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
  template: driverquery /?
  sandbox: execFile
examples:
- description: Run driverquery with default options
  command: driverquery /?
references:
- label: driverquery Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/driverquery
---
