---
id: net-tcpflow
namespace: network:capture:traffic
name: tcpflow
description: Captures TCP connections and reconstructs data streams.
version: 1.0.0
capabilities:
- network.diagnostics
- network.configuration
- system.information-gathering
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: tcpflow --help
  sandbox: execFile
examples:
- description: Display help for tcpflow
  command: tcpflow --help
references:
- label: tcpflow Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tcpflow
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y tcpflow
---
