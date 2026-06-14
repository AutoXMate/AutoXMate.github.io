---
id: pathping
namespace: network:diagnostic
name: pathping
description: Combines ping and tracert functionality to provide packet loss information and latency at each hop.
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
        pathping
  background_templates: []
examples:
  - cmd: "pathping /?"
    description: "Display help and usage information for pathping"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pathping
---