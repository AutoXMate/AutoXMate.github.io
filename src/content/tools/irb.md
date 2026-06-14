---
id: runtime-irb
namespace: runtime:ruby:irb
name: irb
description: Interactive Ruby shell, can execute arbitrary Ruby code.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - ruby
  - pry
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell output
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
  - irb
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: 'irb -e "exec \"/bin/sh\""'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via irb
    command: irb -e 'exec "/bin/sh"'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/irb/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "ruby"
    commands:
      - "apt-get install -y ruby"
---
