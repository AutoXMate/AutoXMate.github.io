---
id: windows-bypass-wfc
namespace: windows:bypass:wfc
name: wfc
description: 'The Workflow Command-line Compiler tool is included with the Windows Software Development Kit (SDK). Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe.'
author: Jimmy (@bohops)
version: 1.0.0
capabilities:
- security.defense-evasion.bypass
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
- wfc
parameters: []
features: []
execution:
  template: wfc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute arbitrary C# code embedded in a XOML file. (Execute proxied payload with Microsoft signed binary to bypass WDAC policies)
  command: wfc.exe {PATH_ABSOLUTE:.xoml}
references:
- label: ''
  url: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
techniques:
- defense-evasion
mitre_ids:
- T1127
detections:
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml
- type: ioc
  description: As a Windows SDK binary, execution on a system may be suspicious
install:
- method: choco
  package_name: wfc
  commands:
  - choco install wfc
---


# wfc

wfc is a Windows LOLBin. The Workflow Command-line Compiler tool is included with the Windows Software Development Kit (SDK). Located at: C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe.
