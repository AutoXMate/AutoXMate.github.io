---
id: dev-vcs-hg
namespace: dev:vcs:hg
name: hg
description: Mercurial VCS, can execute Python code via hgrc or hooks.
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
  - git
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
  - hg
  - python
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "hg -R /path/to/repo"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Python code via hg
    command: hg -R /path/to/repo
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/hg/"
techniques:
  - execution
install:
  - method: apt
    package_name: "mercurial"
    commands:
      - "apt-get install -y mercurial"
---
