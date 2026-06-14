---
id: nltest
namespace: security:ad:trust
name: nltest
description: Network test tool for querying and managing Active Directory trust relationships and secure channels.
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
        nltest
  background_templates: []
examples:
  - cmd: "nltest /?"
    description: "Display help and usage information for nltest"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nltest
---