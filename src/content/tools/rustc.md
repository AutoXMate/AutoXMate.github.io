---
id: build-compiler-rustc
namespace: build:compiler:rustc
name: rustc
description: Rust compiler, can execute code via compiled binaries.
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
  - rustdoc
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
      description: Binary execution output
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
  - rustc
  - rustdoc
  - rustfmt
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "rustc /path/to/src.rs -o /tmp/output && /tmp/output"
  sandbox: execFile
  timeout_seconds: 120
  shell: false
global_vars: {}
examples:
  - description: Execute command via rustc compiled binary
    command: |
      echo 'fn main() { std::process::Command::new("/bin/sh").status().unwrap(); }' >x.rs
      rustc x.rs && ./x
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/rustc/"
techniques:
  - execution
install:
  - method: apt
    package_name: "rustc"
    commands:
      - "apt-get install -y rustc"
---
