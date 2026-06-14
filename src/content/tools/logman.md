---
id: logman
namespace: system:windows:performance
name: logman
description: Manages Performance Monitor logs and traces. Creates, starts, stops, and queries performance data collector sets.
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
        logman
  background_templates: []
examples:
  - cmd: "logman /?"
    description: "Display help and usage information for logman"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman
---