---
id: windows-conceal-devicecredentialdeployment
namespace: windows:conceal:devicecredentialdeployment
name: devicecredentialdeployment
description: 'Device Credential Deployment Located at: C:\Windows\System32\DeviceCredentialDeployment.exe.'
author: Elliot Killick
version: 1.0.0
capabilities:
- security.defense-evasion.conceal
platforms:
- windows
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
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
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- devicecredentialdeployment
parameters: []
features:
- pipes-stdout
execution:
  template: devicecredentialdeployment
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Grab the console window handle and set it to hidden (Can be used to
    stealthily run a console application (e.g. cmd.exe) in the background)
  command: DeviceCredentialDeployment
references: []
techniques:
- defense-evasion
mitre_ids:
- T1564
detections:
- type: ioc
  description: DeviceCredentialDeployment.exe should not be run on a normal workstation
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_device_credential_deployment.yml
install:
- method: choco
  package_name: devicecredentialdeployment
  commands:
  - choco install devicecredentialdeployment
---

# devicecredentialdeployment

devicecredentialdeployment is a Windows LOLBin. Device Credential Deployment Located at: C:\Windows\System32\DeviceCredentialDeployment.exe.
