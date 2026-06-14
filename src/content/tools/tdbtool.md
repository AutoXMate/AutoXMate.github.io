---
id: database-samba-tdbtool
namespace: database:samba:tdbtool
name: tdbtool
description: Samba TDB database manipulation tool; can read and write files.
author: GTFOBins
version: 1.0.0
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
- tdbtool
parameters: []
features:
- file-system
- interactive
- local
- requires-root
execution:
  template: tdbtool
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: 'tdbtool

    ! /bin/sh'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tdbtool/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: tdb-tools
  commands:
  - apt-get install -y tdb-tools
---

# tdbtool

tdbtool is a command-line utility. Samba TDB database manipulation tool; can also spawn an interactive shell.
