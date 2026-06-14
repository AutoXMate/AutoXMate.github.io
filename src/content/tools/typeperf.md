---
id: typeperf
namespace: system:windows:performance
name: typeperf
description: Performance monitoring tool that writes performance counter data to the command window or a log file.
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
        typeperf
  background_templates: []
examples:
  - cmd: "typeperf /?"
    description: "Display help and usage information for typeperf"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/typeperf
---