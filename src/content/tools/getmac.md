---
id: win-getmac
namespace: network:interface:mac
name: getmac
description: Returns MAC addresses of network adapters.
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
  template: getmac /?
  sandbox: execFile
examples:
- description: Display help for getmac
  command: getmac /?
references:
- label: getmac Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/getmac
---
