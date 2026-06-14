---
id: runtime-ruby-pry
namespace: runtime:ruby:pry
name: pry
description: Interactive Ruby shell with introspection, can execute Ruby code.
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
  - irb
  - ruby
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
      description: Ruby code output
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
  - pry
  - irb
  - ruby
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - process-manip
execution:
  template: 'pry -e "exec \"/bin/sh\""'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via pry
    command: pry -e 'exec "/bin/sh"'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/pry/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: gem
    package_name: "pry"
    commands:
      - "gem install pry"
---
