---
id: lang-perl-cpan
namespace: lang:perl:cpan
name: cpan
description: Perl module installer, can execute Perl code inherited from Perl binary.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.execution.command
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
  - perl
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
      description: Perl code execution output
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
  - cpan
  - perl
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: "cpan"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Execute Perl code via cpan shell escape
    command: |
      cpan
      ! system("/bin/sh")
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/cpan/"
techniques:
  - execution
install:
  - method: apt
    package_name: "perl"
    commands:
      - "apt-get install -y perl"
---
