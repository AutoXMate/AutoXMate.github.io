---
id: system-file-chattr
namespace: system:file:chattr
name: chattr
description: Change file attributes on Linux ext2/ext3/ext4 filesystems, can make files immutable for privilege escalation.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.defense-evasion
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
  - lsattr
artifacts: []
workflow_edges:
  produces: []
  consumes:
    - file
contract:
  inputs:
    - type: system.file.path
      description: Path to target file
  outputs:
    - type: process.output
      description: Command output
  side_effects:
    - filesystem_write
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
  - chattr
  - Bash
  - execFile
parameters:
  - name: file
    type: file
    required: true
    description: "File to make immutable"
features:
  - file-system
execution:
  template: "chattr +i {file}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Make a file immutable
    command: chattr +i /path/to/input-file
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/chattr/"
techniques:
  - defense-evasion
install:
  - method: apt
    package_name: "e2fsprogs"
    commands:
      - "apt-get install -y e2fsprogs"
---
