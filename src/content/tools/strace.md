---
id: sys-strace
namespace: system:linux:trace
name: strace
description: System call tracer for Linux.
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
  template: strace --help
  sandbox: execFile
examples:
- description: Display help for strace
  command: strace --help
references:
- label: strace Documentation
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/strace
- label: strace manual
  url: https://man7.org/linux/man-pages/man1/strace.1.html
install:
- method: custom
  description: Install via package manager
  commands:
  - apt-get install -y strace
---
