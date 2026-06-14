---
id: automation-config-ansible-playbook
namespace: automation:config:ansible-playbook
name: ansible-playbook
description: Ansible playbook executor that can spawn a shell via crafted playbook with shell tasks.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.execution.command
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
  - ansible-test
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - playbook-file
contract:
  inputs:
    - type: system.file.path
      description: Path to ansible playbook
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - ansible-playbook
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "ansible-playbook {0}"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn interactive shell via crafted playbook
    command: |-
      echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >/path/to/temp-file
      ansible-playbook /path/to/temp-file
references:
  - label: "Ansible playbook documentation"
    url: "https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: pip
      commands:
        - "pip install ansible"
---


# ansible-playbook — Ansible Playbook Runner

Executes Ansible playbooks. By crafting a playbook with a shell task, it can spawn an interactive shell when used with sudo.
