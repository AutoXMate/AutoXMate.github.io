---
id: security-apparmor-aa-exec
namespace: security:apparmor:aa-exec
name: aa-exec
description: Run a program with a specified AppArmor profile, can spawn a shell when used with sudo or SUID.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
    - shell-access
  consumes:
    - execution-context
contract:
  inputs:
    - type: security.apparmor.profile
      description: AppArmor profile to execute under
  outputs:
    - type: process.output
      description: Shell or command output
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
  - aa-exec
  - Bash
  - execFile
parameters:
  - name: profile
    type: string
    required: false
    description: "AppArmor profile to use"
    aliases:
      - -p
      - --profile
features:
  - process-manip
execution:
  template: "aa-exec {profile}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn an interactive shell under AppArmor confinement
    command: aa-exec /bin/sh
  - description: Run a command under a specific AppArmor profile
    command: aa-exec -p /usr/bin/ping
references:
  - label: "AppArmor wiki"
    url: "https://wiki.ubuntu.com/AppArmor"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "apparmor-utils"
      commands:
        - "apt-get install -y apparmor-utils"
---


# aa-exec — AppArmor Profile Execution

aa-exec runs a program with a specified AppArmor profile. When installed with SUID or available via sudo, it can be used to spawn a shell.

## Privilege Escalation

```bash
# Spawn interactive shell
aa-exec /bin/sh
```
