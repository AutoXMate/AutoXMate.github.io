---
id: set
namespace: system:windows:cmd
name: set
description: Displays, sets, or removes environment variables. Used without parameters, displays all current environment variables.
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
        set
  background_templates: []
examples:
  - cmd: "set"
    description: "Display all environment variables"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set
---