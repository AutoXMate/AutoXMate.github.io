---
id: system-emulator-dosbox
namespace: system:emulator:dosbox
name: dosbox
description: DOS emulator, can read and write files via mounted host filesystem.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
  - system.file.write
platforms:
  - linux
  - macos
  - windows
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects:
    - filesystem_write
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - dosbox
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "dosbox -c 'mount c /' -c 'type c:\\path\\to\\input'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via dosbox
    command: dosbox -c 'mount c /' -c 'type c:\path\to\input'
  - description: Write to a file via dosbox
    command: dosbox -c 'mount c /' -c "echo DATA >c:\path\to\output" -c exit
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dosbox/"
techniques:
  - collection
install:
  - method: apt
    package_name: "dosbox"
    commands:
      - "apt-get install -y dosbox"
---
