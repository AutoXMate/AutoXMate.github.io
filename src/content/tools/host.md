---
id: net-host
namespace: network:dns:lookup
name: host
description: Simple DNS lookup for forward and reverse lookups.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
- macos
features:
- local
mitre_ids:
- T1590
parameters: []
execution:
  template: host example.com
  sandbox: execFile
examples:
- description: Lookup DNS records
  command: host example.com
references:
- label: host Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/host
- label: host manual
  url: https://man7.org/linux/man-pages/man1/host.1.html
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y bind9-dnsutils
---
