---
id: sys-fuser
namespace: system:linux:process
name: fuser
description: Identifies processes using files or sockets.
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
  template: fuser --help
  sandbox: execFile
examples:
- description: Display help for fuser
  command: fuser --help
references:
- label: fuser Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fuser
- label: fuser manual
  url: https://man7.org/linux/man-pages/man1/fuser.1.html
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y psmisc
---
