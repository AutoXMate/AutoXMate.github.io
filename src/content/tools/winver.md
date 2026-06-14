---
id: win-winver
namespace: system:windows:info
name: winver
description: Displays Windows version and build information.
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
  template: winver /?
  sandbox: execFile
examples:
- description: Display help for winver
  command: winver /?
references:
- label: winver Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winver
---
