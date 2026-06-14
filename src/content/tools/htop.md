---
id: htop
namespace: system:linux:monitor
name: htop
description: Interactive process viewer and manager. An enhanced version of top with color output and mouse support.
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
      - "apt-get install -y htop"
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        htop
  background_templates: []
examples:
  - cmd: "htop --help"
    description: "Display help and usage information for htop"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/htop
---