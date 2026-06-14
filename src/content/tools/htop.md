---
id: sys-htop
namespace: system:linux:monitor
name: htop
description: Interactive process viewer and manager.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
- macos
features:
- local
mitre_ids: []
parameters: []
execution:
  template: htop
  sandbox: execFile
examples:
- description: Interactive process viewer
  command: htop
references:
- label: htop Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/htop
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y htop
---
