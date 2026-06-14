---
id: build-cmake-cmake
namespace: build:cmake:cmake
name: cmake
description: Cross-platform build system generator, can read files and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
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
  - make
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or file output
  side_effects:
    - process_spawn
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
  - cmake
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "cmake -E cat {input}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via cmake
    command: cmake -E cat /path/to/input-file
  - description: Spawn a shell via cmake
    command: |
      echo 'execute_process(COMMAND /bin/sh)' >/path/to/CMakeLists.txt
      cmake /path/to/
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cmake/"
techniques:
  - collection
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "cmake"
    commands:
      - "apt-get install -y cmake"
---
