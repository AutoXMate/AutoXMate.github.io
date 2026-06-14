---
id: ipconfig
namespace: network:windows:config
name: ipconfig
description: Displays all current TCP/IP network configuration values and refreshes DHCP and DNS settings.
version: "1.0.0"
capabilities:
  - windows-command
  - system-administration
  - information-gathering
features:
  - local
  - batch
install:
  - method: native
    commands:
      - ""
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        ipconfig
  background_templates: []
examples:
  - cmd: "ipconfig /?"
    description: "Display full TCP/IP configuration"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig
---