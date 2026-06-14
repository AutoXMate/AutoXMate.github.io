---
id: encode-uuencode-uuencode
namespace: encode:uuencode:uuencode
name: uuencode
description: Encode binary files for email transmission; can read arbitrary files.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- uuencode
parameters: []
features:
- file-system
- local
execution:
  template: uuencode
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: uuencode /path/to/input-file /dev/stdout | uudecode
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/uuencode/
techniques:
- collection
install:
- method: apt
  package_name: sharutils
  commands:
  - apt-get install -y sharutils
---

# uuencode

uuencode is a command-line utility. Encode binary files for email transmission; can also read arbitrary files.
