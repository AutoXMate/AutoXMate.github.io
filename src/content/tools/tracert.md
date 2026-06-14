---
id: tracert
namespace: network:diagnostic
name: tracert
description: Traces the route packets take to a network destination by sending ICMP echo requests with incrementing TTL values.
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
        tracert
  background_templates: []
examples:
  - cmd: "tracert /?"
    description: "Display help and usage information for tracert"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert
---