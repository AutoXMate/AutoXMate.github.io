---
id: security-privilege-pkexec
namespace: security:privilege:pkexec
name: pkexec
description: Execute command as another user via polkit, can spawn root shell.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - sudo
  - doas
  - ksu
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
  - pkexec
  - sudo
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "pkexec /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a root shell via pkexec
    command: pkexec /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pkexec/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "policykit-1"
    commands:
      - "apt-get install -y policykit-1"
---
