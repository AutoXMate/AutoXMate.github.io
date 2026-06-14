---
id: dsquery
namespace: security:ad:query
name: dsquery
description: Active Directory query tool that retrieves objects from the directory using specified criteria.
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
        dsquery
  background_templates: []
examples:
  - cmd: "dsquery /?"
    description: "Display help and usage information for dsquery"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dsquery
---