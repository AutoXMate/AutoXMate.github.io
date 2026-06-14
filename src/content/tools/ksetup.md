---
id: win-ksetup
namespace: security:kerberos:config
name: ksetup
description: Configures Kerberos realm mappings and encryption types.
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
  template: ksetup /?
  sandbox: execFile
examples:
- description: Display help for ksetup
  command: ksetup /?
references:
- label: ksetup Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ksetup
---
