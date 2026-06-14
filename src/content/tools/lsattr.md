---
id: lsattr
namespace: system:linux:file
name: lsattr
description: Lists file attributes on a Linux ext2/ext3/ext4 file system.
version: "1.0.0"
capabilities:
  - system-administration
  - information-gathering
  - file-system
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
        lsattr
  background_templates: []
examples:
  - cmd: "lsattr --help"
    description: "Display help and usage information for lsattr"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsattr
---