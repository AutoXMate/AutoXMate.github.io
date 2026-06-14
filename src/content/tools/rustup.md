---
id: build-compiler-rustup
namespace: build:compiler:rustup
name: rustup
description: Rust toolchain manager, can execute commands.
author: "GTFOBins"
version: "1.0.0"
capabilities:
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
  - rustc
  - rustdoc
  - rustfmt
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
  - rustup
  - rustc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rustup run /path/to/command"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via rustup
    command: rustup run /path/to/command
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rustup/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rustup"
    commands:
      - "apt-get install -y rustup"
---
