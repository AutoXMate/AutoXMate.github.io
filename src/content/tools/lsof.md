---
id: lsof
namespace: system:linux:process
name: lsof
description: Lists open files and the processes that opened them. Useful for finding which processes have specific files or network connections open.
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
      - "apt-get install -y lsof"
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        lsof
  background_templates: []
examples:
  - cmd: "lsof --help"
    description: "Display help for lsof"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/lsof
---