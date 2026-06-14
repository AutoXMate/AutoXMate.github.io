---
id: sys-lsof
namespace: system:linux:process
name: lsof
description: Lists open files and the processes that opened them.
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
  template: lsof
  sandbox: execFile
examples:
- description: List open files
  command: lsof
references:
- label: lsof Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsof
- label: lsof manual
  url: https://man7.org/linux/man-pages/man1/lsof.1.html
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y lsof
---
