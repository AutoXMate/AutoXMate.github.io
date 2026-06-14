---
id: host
namespace: network:dns
name: host
description: Simple DNS lookup utility that performs forward and reverse DNS lookups.
version: "1.0.0"
capabilities:
  - network-diagnostics
  - information-gathering
  - reconnaissance
features:
  - local
  - batch
install:
  - method: apt
    commands:
      - "apt-get install -y bind9-host"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        host
  background_templates: []
examples:
  - cmd: "host --help"
    description: "Lookup DNS records for a domain"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/host
---