---
id: where
namespace: system:windows:file
name: where
description: Displays the location of files that match the search pattern, similar to Unix 'which' but with broader search capabilities.
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
        where
  background_templates: []
examples:
  - cmd: "where ."
    description: "Display help and usage information for where"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where
---