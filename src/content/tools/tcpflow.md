---
id: tcpflow
namespace: network:capture
name: tcpflow
description: TCP flow recorder that captures TCP connections and reconstructs the data streams for analysis.
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
      - "apt-get install -y tcpflow"
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        tcpflow
  background_templates: []
examples:
  - cmd: "tcpflow --help"
    description: "Display help and usage information for tcpflow"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tcpflow
---