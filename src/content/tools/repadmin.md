---
id: cmd-repadmin
namespace: security:ad:replication
name: repadmin
description: Active Directory replication diagnostics and management tool.
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
  template: repadmin /?
  sandbox: execFile
examples:
- description: Run repadmin with default options
  command: repadmin /?
references:
- label: repadmin Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/repadmin
---
