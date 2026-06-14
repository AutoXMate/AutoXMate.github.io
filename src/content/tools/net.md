---
id: net
namespace: system:windows:networking
name: net
description: Comprehensive network and system administration command used for managing users, groups, shares, services, and network connections.
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
        net
  background_templates: []
examples:
  - cmd: "net /?"
    description: "List user accounts"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net
---