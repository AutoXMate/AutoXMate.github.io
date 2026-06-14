---
id: network-http-nginx
namespace: network:http:nginx
name: nginx
description: Web server, can read files and execute commands via modules.
author: GTFOBins
version: 1.0.0
capabilities:
- system.file.read
- security.execution.command
platforms:
- linux
- bsd
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- apache2
artifacts: []
workflow_edges:
  produces:
  - file-content
  - command-execution
  consumes:
  - file
  - execution-context
contract:
  inputs: []
  outputs:
  - type: process.output
    description: File or command output
  side_effects:
  - process_spawn
  - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- nginx
- Bash
- execFile
parameters: []
features:
- file-system
- process-manip
- requires-root
execution:
  template: nginx -c /path/to/config
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Read a file via nginx
  command: nginx -c /path/to/file
- description: Execute command via nginx
  command: nginx -c /path/to/config
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/nginx/
techniques:
- collection
- execution
install:
- method: apt
  package_name: nginx
  commands:
  - apt-get install -y nginx
mitre_ids:
- T1005
- T1046
- T1048
- T1074
- T1114
- T1190
- T1595
---


