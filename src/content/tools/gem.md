---
id: package-ruby-gem
namespace: package:ruby:gem
name: gem
description: Ruby package manager that can spawn shells via editor open or install hooks.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
  - system.package.install
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - ruby
  - bundler
  - rake
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - gem-name
contract:
  inputs:
    - type: system.package.ruby
      description: Ruby gem name
  outputs:
    - type: process.output
      description: Shell output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
  - gem
  - Bash
  - execFile
parameters:
  - name: open
    type: string
    required: false
    description: "Open gem source directory"
    aliases:
      - open
  - name: e
    type: string
    required: false
    description: "Editor to use"
    aliases:
      - -e
  - name: build
    type: file
    required: false
    description: "Build a gem from a gemspec"
    aliases:
      - build
  - name: install
    type: string
    required: false
    description: "Install a gem"
    aliases:
      - install
  - name: file
    type: file
    required: false
    description: "Install from file"
    aliases:
      - --file
features:
  - process-manip
execution:
  template: "gem {open} {e} {build} {install} {file}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn shell via gem open with custom editor
    command: gem open -e '/bin/sh -s' debug
  - description: Execute ruby code via gem build (inherits from ruby)
    command: gem build /path/to/script.rb
  - description: Execute ruby code via gem install --file
    command: gem install --file /path/to/script.rb
  - description: Open vi editor via gem open (can escape to shell)
    command: gem open debug
references:
  - label: "RubyGems documentation"
    url: "https://guides.rubygems.org/"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "ruby"
      commands:
        - "apt-get install -y ruby"
---


# gem — Ruby Package Manager

gem manages Ruby packages. The `open` command with a custom editor flag can spawn a shell. The `build` and `install --file` commands inherit from Ruby, allowing arbitrary code execution when used with sudo.
