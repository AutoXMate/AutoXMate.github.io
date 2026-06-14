---
id: bootcfg
namespace: system:windows:boot
name: bootcfg
description: Configures, queries, or changes Boot.ini file settings for multi-boot systems.
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
        bootcfg
  background_templates: []
examples:
  - cmd: "bootcfg /?"
    description: "Display help and usage information for bootcfg"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bootcfg
---