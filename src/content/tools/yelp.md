---
id: system-help-yelp
namespace: system:help:yelp
name: yelp
description: GNOME help viewer; can read arbitrary files.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
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
- yelp
parameters: []
features:
- file-system
- local
execution:
  template: yelp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read arbitrary files (sudo, unprivileged)
  command: yelp man:/path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/yelp/
techniques:
- collection
install:
- method: apt
  package_name: yelp
  commands:
  - apt-get install -y yelp
---

# yelp

yelp is a command-line utility. GNOME help viewer; can also read arbitrary files.
