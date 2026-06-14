---
id: system-tui-dialog
namespace: system:tui:dialog
name: dialog
description: Display dialog boxes from shell scripts, can read files via the --textbox option.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - whiptail
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs:
    - type: system.file.path
      description: Path to input file
  outputs:
    - type: process.output
      description: File content in TUI
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - dialog
  - Bash
  - execFile
parameters:
  - name: input
    type: file
    required: false
    description: "File to display"
features:
  - interactive
execution:
  template: "dialog --textbox {input} 0 0"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via dialog textbox
    command: dialog --textbox /path/to/input-file 0 0
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dialog/"
techniques:
  - collection
install:
  - method: apt
    package_name: "dialog"
    commands:
      - "apt-get install -y dialog"
---
