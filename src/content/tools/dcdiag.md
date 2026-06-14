---
id: dcdiag
namespace: security:ad:diagnostic
name: dcdiag
description: Domain Controller diagnostics tool that analyzes the state of domain controllers in an Active Directory forest.
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
        dcdiag
  background_templates: []
examples:
  - cmd: "dcdiag /?"
    description: "Display help and usage information for dcdiag"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dcdiag
---