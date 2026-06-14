---
id: xclip
namespace: system:linux:clipboard
name: xclip
description: Command-line interface to the X11 clipboard. Pipes data to/from the clipboard selection buffers.
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
      - "apt-get install -y xclip"
mitre_ids: []
parameters: []
execution:
  method: shell
  templates:
    - template: |
        xclip
  background_templates: []
examples:
  - cmd: "xclip --help"
    description: "Display help and usage information for xclip"
references:
  - https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xclip
---