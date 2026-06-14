---
id: wusa
namespace: system:windows:update
name: wusa
description: Windows Update Standalone Installer for installing, uninstalling, and listing Windows update packages.
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
        wusa
  background_templates: []
examples:
  - cmd: "wusa /?"
    description: "Display help and usage information for wusa"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wusa
---