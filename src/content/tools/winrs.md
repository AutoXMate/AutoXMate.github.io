---
id: win-winrs
namespace: remote:winrm:shell
name: winrs
description: Windows Remote Shell via WinRM.
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
  template: winrs /?
  sandbox: execFile
examples:
- description: Display help for winrs
  command: winrs /?
references:
- label: winrs Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winrs
---
