---
id: lodctr
namespace: system:windows:performance
name: lodctr
description: Allows registering or unregistering performance counter names and explanation text for system services.
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
        lodctr
  background_templates: []
examples:
  - cmd: "lodctr /?"
    description: "Display help and usage information for lodctr"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lodctr
---