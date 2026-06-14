---
id: package-pkg-pkg
namespace: package:pkg:pkg
name: pkg
description: FreeBSD package manager, can execute commands via pre/post-install scripts.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - bsd
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - pkg_add
  - pkg_install
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
  - pkg
  - pkg_add
  - Bash
  - execFile
parameters: []
features:
  - requires-root
  - process-manip
execution:
  template: "pkg install -y /path/to/package.txz"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via pkg with crafted package
    command: pkg install -y /path/to/package.txz
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pkg/"
techniques:
  - execution
install:
  - method: apt
    package_name: "pkg"
    commands:
      - "apt-get install -y pkg"
---
