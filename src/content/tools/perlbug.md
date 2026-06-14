---
id: dev-perl-perlbug
namespace: dev:perl:perlbug
name: perlbug
description: Perl bug reporting tool, can execute commands.
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
  - perl
  - cpan
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
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - perlbug
  - perl
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "perlbug /path/to/report"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute command via perlbug
    command: perlbug /path/to/report
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/perlbug/"
techniques:
  - execution
install:
  - method: apt
    package_name: "perl"
    commands:
      - "apt-get install -y perl"
---
