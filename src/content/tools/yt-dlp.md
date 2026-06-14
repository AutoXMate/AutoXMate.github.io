---
id: network-download-yt-dlp
namespace: network:download:yt-dlp
name: yt-dlp
description: "Download videos from YouTube and other sites; can execute arbitrary commands."
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
- yt-dlp
parameters: []
features: []
execution:
  template: yt-dlp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Spawn an interactive shell (sudo, unprivileged)
  command: 'yt-dlp ''https://www.youtube.com/watch?v=xxxxxxxxxxx'' --exec ''/bin/sh #'''
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/yt-dlp/
techniques:
- privilege-escalation
- execution
install:
- method: apt
  package_name: yt-dlp
  commands:
  - apt-get install -y yt-dlp
---


# yt-dlp

yt-dlp is a command-line utility. Download videos from YouTube and other sites; can also spawn an interactive shell.
