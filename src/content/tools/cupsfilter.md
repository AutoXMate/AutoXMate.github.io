---
id: system-print-cupsfilter
namespace: system:print:cupsfilter
name: cupsfilter
description: CUPS filter/converter, can read files via format conversion.
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
related_tools:
- cancel
- lp
artifacts: []
workflow_edges:
  produces:
  - file-content
  consumes:
  - file
contract:
  inputs:
  - type: system.file.path
    description: Path to input file
  outputs:
  - type: process.output
    description: File content output
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 8
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: none
  disk_io: low
allowed-tools:
- cupsfilter
- Bash
- execFile
parameters:
- name: input
  type: file
  required: false
  description: File to read
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: cupsfilter -i application/octet-stream -m application/octet-stream {input}
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via cupsfilter
  command: cupsfilter -i application/octet-stream -m application/octet-stream /path/to/input-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/cupsfilter/
techniques:
- collection
install:
- method: apt
  package_name: cups
  commands:
  - apt-get install -y cups
---


