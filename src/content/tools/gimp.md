---
id: image-edit-gimp
namespace: image:edit:gimp
name: gimp
description: GNU Image Manipulation Program, can execute scripts via Script-Fu.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
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
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Script execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 64
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 64
  network: none
  disk_io: low
allowed-tools:
  - gimp
  - Bash
  - execFile
parameters: []
features:
  - process-manip
  - interactive
execution:
  template: "gimp -b '(command)'"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute Scheme script via gimp
    command: gimp -b '(command)'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gimp/"
techniques:
  - execution
install:
  - method: apt
    package_name: "gimp"
    commands:
      - "apt-get install -y gimp"
---
