---
id: runtime-ruby-ruby
namespace: runtime:ruby:ruby
name: ruby
description: Ruby interpreter, can execute Ruby code and spawn shells.
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
  - irb
  - pry
  - gem
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - file-content
  consumes:
    - execution-context
    - file
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
  - ruby
  - irb
  - gem
  - Bash
  - execFile
parameters: []
features:
  - interactive
  - file-system
  - process-manip
execution:
  template: 'ruby -e "exec \"/bin/sh\""'
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via ruby
    command: ruby -e 'exec "/bin/sh"'
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/ruby/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "ruby"
    commands:
      - "apt-get install -y ruby"
---
