---
id: gunzip
namespace: archive:compression
name: gunzip
description: Decompresses files compressed with gzip (.gz). Equivalent to gzip -d.
version: "1.0.0"
capabilities:
  - compression
  - file-system
  - data-transfer
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
  method: shell
  templates:
    - template: |
        gunzip
  background_templates: []
examples:
  - cmd: "gunzip --help"
    description: "Display help and usage information for gunzip"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gunzip
---