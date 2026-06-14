---
id: dir
namespace: system:windows:file
name: dir
description: Displays a list of files and subdirectories in a directory. Supports various sorting and filtering options.
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
        dir
  background_templates: []
examples:
  - cmd: "dir ."
    description: "List files in bare format"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dir
---