---
id: runtime-perl-perl
namespace: runtime:perl:perl
name: perl
description: Perl interpreter, can execute arbitrary Perl code and spawn shells.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - system.file.read
  - system.file.write
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
  - perlbug
  - cpan
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
    - command-execution
  consumes:
    - execution-context
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Perl code output
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
  - perl
  - perlbug
  - cpan
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - file-system
  - process-manip
execution:
  template: "perl -e 'exec \"/bin/sh\"'"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via perl
    command: perl -e 'exec "/bin/sh"'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/perl/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "perl"
    commands:
      - "apt-get install -y perl"
---
