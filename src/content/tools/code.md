---
id: dev-vscode-code
namespace: dev:vscode:code
name: code
description: Visual Studio Code editor; can spawn a shell and execute commands via
  integrated terminal Can also download files, send a reverse shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- security.execution.reverse-shell
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
- code
parameters: []
features:
- file-system
- interactive
- local
- network-intensive
- pipes-stdin
- process-manip
execution:
  template: code
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: code tunnel --name xxxxxx
- description: Send a reverse shell
  command: code tunnel --name xxxxxx
- description: Upload files
  command: code tunnel --name xxxxxx
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/code/
techniques:
- collection
- command-and-control
- execution
- exfiltration
install:
- method: apt
  package_name: code
  commands:
  - apt-get install -y code
---

# code

code is a command-line utility. Visual Studio Code editor; can spawn a shell and execute commands via integrated terminal Can also download files, send a reverse shell, upload files.
