---
id: dev-rust-cargo
namespace: dev:rust:cargo
name: cargo
description: Rust package manager, can read files via pager (less) inheritance.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - macos
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - less
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs:
    - type: system.file.path
      description: Path to file to read
  outputs:
    - type: process.output
      description: File content
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: none
  disk_io: low
allowed-tools:
  - cargo
  - less
  - Bash
  - execFile
parameters: []
features:
  - file-system
execution:
  template: "cargo help doc"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read a file via cargo pager
    command: cargo help doc
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cargo/"
techniques:
  - collection
install:
  - method: apt
    package_name: "cargo"
    commands:
      - "apt-get install -y cargo"
  - method: brew
    package_name: "rust"
    commands:
      - "brew install rust"
---
