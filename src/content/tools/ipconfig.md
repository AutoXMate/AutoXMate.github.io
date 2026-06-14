---
id: cmd-ipconfig
namespace: network:windows:config
name: ipconfig
description: Displays all current TCP/IP network configuration values and refreshes
  DHCP and DNS settings.
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
- T1015
parameters: []
execution:
  template: ipconfig /?
  sandbox: execFile
examples:
- description: Run ipconfig with default options
  command: ipconfig /?
references:
- label: ipconfig Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig
---
