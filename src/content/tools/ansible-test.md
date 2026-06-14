---
id: automation-config-ansible-test
namespace: automation:config:ansible-test
name: ansible-test
description: Ansible testing tool that can spawn a shell directly via the shell subcommand.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
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
  - ansible-playbook
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes: []
contract:
  inputs: []
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
  - ansible-test
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "ansible-test {0}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell
    command: ansible-test shell
references:
  - label: "Ansible-test documentation"
    url: "https://docs.ansible.com/ansible/latest/cli/ansible-test.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: pip
      commands:
        - "pip install ansible"
---


# ansible-test — Ansible Testing Tool

Part of the Ansible testing framework. The `shell` subcommand spawns an interactive shell, useful for privilege escalation when the binary has sudo access.
