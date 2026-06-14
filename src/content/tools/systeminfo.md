---
id: systeminfo
namespace: system:windows:cmd
name: systeminfo
description: Displays detailed operating system configuration information including OS version, build number, service pack level, and system hardware specs.
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
        systeminfo
  background_templates: []
examples:
  - cmd: "systeminfo"
    description: "Display system information"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo
---