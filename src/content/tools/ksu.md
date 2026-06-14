---
id: security-privilege-ksu
namespace: security:privilege:ksu
name: ksu
description: Kerberized superuser, can execute commands as another user.
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
  - su
  - doas
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
  - ksu
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "ksu -e /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ksu
    command: ksu -e /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ksu/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "heimdal-clients"
    commands:
      - "apt-get install -y heimdal-clients"
---
