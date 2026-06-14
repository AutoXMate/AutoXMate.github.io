---
id: strace
namespace: system:linux:trace
name: strace
description: System call tracer for Linux. Intercepts and records system calls made by a process.
version: "1.0.0"
capabilities:
  - system-administration
  - information-gathering
  - file-system
features:
  - local
  - batch
install:
  - method: apt
    commands:
      - "apt-get install -y strace"
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        strace
  background_templates: []
examples:
  - cmd: "strace --help"
    description: "Display help for strace"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/strace
---