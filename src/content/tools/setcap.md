---
id: security-capabilities-setcap
namespace: security:capabilities:setcap
name: setcap
description: Set file capabilities, can execute commands via cap-enabled binaries.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - linux
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - getcap
  - capsh
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
      description: Command execution output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - setcap
  - getcap
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "setcap cap_setuid+ep /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via setcap-enabled binary
    command: setcap cap_setuid+ep /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/setcap/"
techniques:
  - privilege-escalation
install:
  - method: apt
    package_name: "libcap2-bin"
    commands:
      - "apt-get install -y libcap2-bin"
---
