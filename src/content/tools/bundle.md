---
id: dev-ruby-bundle
namespace: dev:ruby:bundle
name: bundle
description: Ruby dependency manager (Bundler), can spawn shells via exec and Gemfile manipulation.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - bundler
  - ruby
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.execution.context
      description: Sudo or unprivileged execution context
  outputs:
    - type: process.output
      description: Shell output
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
  - bundle
  - bundler
  - ruby
  - irb
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "bundle exec /bin/sh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via bundle exec
    command: bundle exec /bin/sh
  - description: Spawn a shell via BUNDLE_GEMFILE trick
    command: BUNDLE_GEMFILE=x bundle exec /bin/sh
  - description: Spawn a shell via Gemfile install hook
    command: |
      echo 'system("/bin/sh")' >Gemfile
      bundle install
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/bundle/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: gem
    package_name: "bundler"
    commands:
      - "gem install bundler"
---
