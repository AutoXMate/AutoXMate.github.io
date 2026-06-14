---
id: system-container-nsenter
namespace: system:container:nsenter
name: nsenter
description: Enter namespaces, can escalate privileges and spawn shells in containers.
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
  - unshare
  - genie
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
  - nsenter
  - unshare
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "nsenter --target <pid> --mount --uts --ipc --net --pid -- /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via nsenter
    command: nsenter --target <pid> --mount --uts --ipc --net --pid -- /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/nsenter/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "util-linux"
    commands:
      - "apt-get install -y util-linux"
---
