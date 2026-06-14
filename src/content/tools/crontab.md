---
id: system-scheduler-crontab
namespace: system:scheduler:crontab
name: crontab
description: Schedule periodic tasks via cron, can execute commands via editor escape or direct scheduling.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.execution.command
  - system.scheduler.cron
  - security.privilege-escalation.shell
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - cron
  - at
artifacts: []
workflow_edges:
  produces:
    - scheduled-task
    - shell-access
  consumes: []
contract:
  inputs: []
  outputs:
    - type: system.scheduler.cron
      description: Scheduled cron job
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - crontab
  - Bash
  - execFile
parameters:
  - name: e
    type: string
    required: false
    description: "Edit crontab"
    aliases:
      - -e
features:
  - process-manip
execution:
  template: "crontab {e}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Edit crontab and schedule a shell command for execution
    command: crontab -e
references:
  - label: "crontab man page"
    url: "https://man7.org/linux/man-pages/man5/crontab.5.html"
techniques:
  - privilege-escalation
  - execution
  - persistence
install:
    - method: apt
      package_name: "cron"
      commands:
        - "apt-get install -y cron"
---


# crontab — Cron Table Manager

crontab manages cron jobs for task scheduling. With `-e`, it opens the default editor (vi) to edit the crontab, where arbitrary commands can be scheduled. Also allows editor escape via vi for shell access.
