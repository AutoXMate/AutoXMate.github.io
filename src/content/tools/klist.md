---
id: klist
namespace: security:kerberos
name: klist
description: Displays the list of currently cached Kerberos tickets for authentication purposes.
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
        klist
  background_templates: []
examples:
  - cmd: "klist /?"
    description: "Display help and usage information for klist"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/klist
---