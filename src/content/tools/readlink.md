---
id: readlink
namespace: system:linux:file
name: readlink
description: Displays the target of a symbolic link or canonical path. Useful for resolving file paths and following symlinks.
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
        readlink
  background_templates: []
examples:
  - cmd: "readlink --help"
    description: "Display help and usage information for readlink"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/readlink
---