---
id: wevtutil
namespace: system:windows:logging
name: wevtutil
description: Retrieves information about event logs and publishers, exports, archives, and clears event logs.
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
        wevtutil
  background_templates: []
examples:
  - cmd: "wevtutil /?"
    description: "Display help and usage information for wevtutil"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil
---