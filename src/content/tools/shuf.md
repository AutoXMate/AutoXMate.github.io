---
id: system-text-shuf
namespace: system:text:shuf
name: shuf
description: Generate random permutations of input lines; can read and write files.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
- system.file.write
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
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
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
- shuf
parameters: []
features:
- file-system
- local
execution:
  template: shuf
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: shuf -z /path/to/input-file
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: shuf -e DATA -o /path/to/output-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/shuf/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: coreutils
  commands:
  - apt-get install -y coreutils
---

# shuf

shuf is a command-line utility. Generate random permutations of input lines; can also read arbitrary files, write to arbitrary files.
