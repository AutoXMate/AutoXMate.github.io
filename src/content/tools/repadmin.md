---
id: repadmin
namespace: security:ad:replication
name: repadmin
description: Active Directory replication diagnostics and management tool for monitoring and troubleshooting AD replication.
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
        repadmin
  background_templates: []
examples:
  - cmd: "repadmin /?"
    description: "Display help and usage information for repadmin"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/repadmin
---