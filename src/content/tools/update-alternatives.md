---
id: system-alternatives-update-alternatives
namespace: system:alternatives:update-alternatives
name: update-alternatives
description: "Manage symbolic links for default commands; can read arbitrary files."
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.write
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
- update-alternatives
parameters: []
features: []
execution:
  template: update-alternatives
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Write to arbitrary files (sudo, suid)
  command: 'echo DATA >/path/to/temp-file

    update-alternatives --force --install /path/to/output-file x /path/to/temp-file 0'
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/update-alternatives/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: dpkg
  commands:
  - apt-get install -y dpkg
---


# update-alternatives

update-alternatives is a command-line utility. Manage symbolic links for default commands; can also write to arbitrary files.
