---
id: diskpart
namespace: system:windows:disk
name: diskpart
description: Command-line disk partitioning utility for managing disks, partitions, volumes, and virtual hard disks.
version: "1.0.0"
capabilities:
  - windows-command
  - system-administration
  - information-gathering
features:
  - local
  - batch
install:
  - method: native
    commands:
      - ""
mitre_ids: []
parameters: []
execution:
  method: cmd
  templates:
    - template: |
        diskpart
  background_templates: []
examples:
  - cmd: "diskpart /?"
    description: "Display help and usage information for diskpart"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart
---