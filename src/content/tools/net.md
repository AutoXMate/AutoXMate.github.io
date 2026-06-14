---
id: cmd-net
namespace: system:windows:networking
name: net
description: Comprehensive network and system administration command used for managing
  users, groups, shares, services, and network connections.
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
  template: net /?
  sandbox: execFile
examples:
- description: Run net with default options
  command: net /?
references:
- label: net Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net
---
