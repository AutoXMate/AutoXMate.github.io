---
id: cmd-systeminfo
namespace: system:windows:cmd
name: systeminfo
description: Displays detailed operating system configuration information including
  OS version, build number, service pack level, and system hardware specs.
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
  template: systeminfo /?
  sandbox: execFile
examples:
- description: Run systeminfo with default options
  command: systeminfo /?
references:
- label: systeminfo Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo
---
