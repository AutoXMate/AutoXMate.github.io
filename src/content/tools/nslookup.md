---
id: nslookup
namespace: network:dns
name: nslookup
description: Queries DNS servers for domain name or IP address resolution. Supports interactive and non-interactive modes.
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
      - "apt-get install -y dnsutils"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        nslookup
  background_templates: []
examples:
  - cmd: "nslookup --help"
    description: "Query DNS for a domain"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup
---