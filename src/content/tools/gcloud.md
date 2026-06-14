---
id: cloud-gcp-gcloud
namespace: cloud:gcp:gcloud
name: gcloud
description: Google Cloud CLI, can execute commands and spawn shells via gcloud compute SSH.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - security.privilege-escalation.shell
  - security.execution.command
platforms:
  - linux
  - macos
risk_level: high
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - gsutil
  - kubectl
artifacts: []
workflow_edges:
  produces:
    - shell-access
    - command-execution
  consumes:
    - execution-context
contract:
  inputs: []
  outputs:
    - type: process.output
      description: Shell or command output
  side_effects:
    - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 32
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: low
  disk_io: low
allowed-tools:
  - gcloud
  - gsutil
  - Bash
  - execFile
parameters: []
features:
  - process-manip
execution:
  template: "gcloud compute ssh [instance] --command /bin/sh"
  sandbox: execFile
  timeout_seconds: 60
  shell: false
global_vars: {}
examples:
  - description: Spawn a shell via gcloud compute ssh
    command: gcloud compute ssh [instance] --command /bin/sh
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/gcloud/"
techniques:
  - privilege-escalation
  - execution
install:
  - method: apt
    package_name: "google-cloud-sdk"
    commands:
      - "apt-get install -y google-cloud-sdk"
---
