---
id: security-privilege-doas
namespace: security:privilege:doas
name: doas
description: Execute commands as another user (OpenBSD-style privilege escalation), can spawn a root shell.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
  - bsd
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - sudo
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
    memory_mb: 2
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 2
  network: none
  disk_io: low
allowed-tools:
  - doas
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "doas -u root /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a root shell via doas
    command: doas -u root /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/doas/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "doas"
    commands:
      - "apt-get install -y doas"
---
