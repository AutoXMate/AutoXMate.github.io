---
id: system-devicemapper-dmsetup
namespace: system:devicemapper:dmsetup
name: dmsetup
description: Device mapper management, can spawn a shell via --exec option.
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
related_tools: []
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - dmsetup
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "dmsetup ls --exec '/bin/sh -s'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via dmsetup --exec
    command: |
      dmsetup create base <<EOF
      0 3534848 linear /dev/loop0 94208
      EOF
      dmsetup ls --exec '/bin/sh -s'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/dmsetup/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "dmsetup"
    commands:
      - "apt-get install -y dmsetup"
---
