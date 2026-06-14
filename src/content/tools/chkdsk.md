---
id: cmd-chkdsk
namespace: system:windows:disk
name: chkdsk
description: Checks a disk for file system errors and bad sectors.
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
  template: chkdsk /?
  sandbox: execFile
examples:
- description: Run chkdsk with default options
  command: chkdsk /?
references:
- label: chkdsk Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk
---
