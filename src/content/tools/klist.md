---
id: win-klist
namespace: security:kerberos:tickets
name: klist
description: Lists cached Kerberos tickets for authentication.
version: 1.0.0
capabilities:
- system.information-gathering
- system.configuration
- system.administration
platforms:
- windows
features:
- local
mitre_ids:
- T1558
parameters: []
execution:
  template: klist /?
  sandbox: execFile
examples:
- description: Display help for klist
  command: klist /?
references:
- label: klist Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/klist
---
