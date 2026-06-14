---
id: net-nslookup
namespace: network:dns:lookup
name: nslookup
description: Queries DNS servers for domain name or IP resolution.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
- windows
features:
- local
mitre_ids:
- T1590
parameters: []
execution:
  template: nslookup example.com
  sandbox: execFile
examples:
- description: Query DNS for a domain
  command: nslookup example.com
references:
- label: nslookup Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y dnsutils
---
