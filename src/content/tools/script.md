---
id: system-terminal-script
namespace: system:terminal:script
name: script
description: Terminal session recorder, can spawn a shell and read/write files.
author: GTFOBins
version: 1.0.0
capabilities:
- security.privilege-escalation.shell
- system.file.read
- system.file.write
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
- tee
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - file-content
  consumes:
  - execution-context
  - file
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Shell or file output
  side_effects:
  - filesystem_write
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
- script
- Bash
- execFile
parameters: []
features:
- interactive
- file-system
- process-manip
execution:
  template: script /dev/null -c /bin/sh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn a shell via script
  command: script /dev/null -c /bin/sh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/script/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: util-linux
  commands:
  - apt-get install -y util-linux
mitre_ids:
- T1059
---


