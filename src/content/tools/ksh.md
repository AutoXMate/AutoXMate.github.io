---
id: shell-ksh-ksh
namespace: shell:ksh:ksh
name: ksh
description: KornShell, can spawn interactive shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
platforms:
  - linux
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - bash
  - sh
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
  - ksh
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "ksh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ksh
    command: ksh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ksh/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "ksh"
    commands:
      - "apt-get install -y ksh"
---
