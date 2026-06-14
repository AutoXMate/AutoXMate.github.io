---
id: build-compiler-rustdoc
namespace: build:compiler:rustdoc
name: rustdoc
description: Rust documentation tool, can execute commands via test code.
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
  - rustfmt
  - rustup
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
    memory_mb: 64
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 64
  network: none
  disk_io: low
allowed-tools:
  - rustdoc
  - rustc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rustdoc /path/to/src.rs --test"
  sandbox: execFile
  timeout_seconds: 120
  shell: false
global_vars: {}
examples:
  - description: Execute command via rustdoc test
    command: rustdoc /path/to/src.rs --test
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rustdoc/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rustc"
    commands:
      - "apt-get install -y rustc"
---
