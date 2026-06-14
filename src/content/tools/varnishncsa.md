---
id: web-cache-varnishncsa
namespace: web:cache:varnishncsa
name: varnishncsa
description: Varnish log viewer in NCSA format; can read arbitrary files.
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
- varnishncsa
parameters: []
features:
- file-system
- local
execution:
  template: varnishncsa
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Write to arbitrary files (sudo, suid)
  command: varnishncsa -g request -q 'ReqURL ~ "/xxxxxxxxxx"' -F '%{yyy}i' -w /path/to/output-file
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/varnishncsa/
techniques:
- collection
- exfiltration
install:
- method: apt
  package_name: varnish
  commands:
  - apt-get install -y varnish
---

# varnishncsa

varnishncsa is a command-line utility. Varnish log viewer in NCSA format; can also write to arbitrary files.
