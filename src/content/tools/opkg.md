---
id: package-opkg-opkg
namespace: package:opkg:opkg
name: opkg
description: OPKG package manager, can execute commands via pre/post-install scripts.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
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
  - dpkg
  - rpm
artifacts: []
workflow_edges:
  produces:
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Command execution output
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
  - opkg
  - dpkg
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "opkg install /path/to/package.ipk"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via opkg with crafted package
    command: opkg install /path/to/package.ipk
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/opkg/"
techniques:
  - execution
install:
  - method: apt
    package_name: "opkg"
    commands:
      - "apt-get install -y opkg"
---
