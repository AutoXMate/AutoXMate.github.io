---
id: fuser
namespace: system:linux:process
name: fuser
description: Identifies processes using files or sockets. Can kill processes that have a file open.
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
      - "apt-get install -y psmisc"
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        fuser
  background_templates: []
examples:
  - cmd: "fuser --help"
    description: "Display help for fuser"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fuser
---