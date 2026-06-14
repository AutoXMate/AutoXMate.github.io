---
id: build-compiler-rustfmt
namespace: build:compiler:rustfmt
name: rustfmt
description: Rust code formatter, can execute commands.
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
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
  - rustfmt
  - rustc
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rustfmt /path/to/file.rs"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Execute command via rustfmt
    command: rustfmt /path/to/file.rs
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rustfmt/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rustfmt"
    commands:
      - "apt-get install -y rustfmt"
---
