---
id: sys-xclip
namespace: system:linux:clipboard
name: xclip
description: CLI interface to the X11 clipboard.
version: 1.0.0
capabilities:
- system.information-gathering
- system.monitoring
- system.administration
platforms:
- linux
features:
- local
mitre_ids: []
parameters: []
execution:
  template: xclip --help
  sandbox: execFile
examples:
- description: Display help for xclip
  command: xclip --help
references:
- label: xclip Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xclip
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y xclip
---
