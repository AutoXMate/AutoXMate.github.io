---
id: sfc
namespace: system:windows:integrity
name: sfc
description: System File Checker scans and verifies protected system files, replacing corrupted versions from the cache.
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
        sfc
  background_templates: []
examples:
  - cmd: "sfc /?"
    description: "Display help and usage information for sfc"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc
---