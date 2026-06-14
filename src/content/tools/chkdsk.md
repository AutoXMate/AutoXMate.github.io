---
id: chkdsk
namespace: system:windows:disk
name: chkdsk
description: Checks a disk for file system errors and bad sectors. Can attempt repairs with appropriate flags.
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
        chkdsk
  background_templates: []
examples:
  - cmd: "chkdsk /?"
    description: "Display help and usage information for chkdsk"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk
---