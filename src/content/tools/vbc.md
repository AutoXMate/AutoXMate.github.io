---
id: windows-compile-vbc
namespace: windows:compile:vbc
name: vbc
description: 'Binary file used for compile vbs code Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe;
  C:\Windows\Microsoft.NET\Framework\v3.5\vbc.exe; C:\Windows\Microsoft.NET\Framework\v2.0.50727\vbc.exe.'
author: Lior Adar
version: 1.0.0
capabilities:
- build.compile.code
platforms:
- windows
risk_level: low
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
- vbc
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: vbc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Binary file used by .NET to compile Visual Basic code to an executable.
    (Compile attacker code on system. Bypass defensive counter measures.)
  command: vbc.exe /target:exe {PATH_ABSOLUTE:.vb}
- description: Binary file used by .NET to compile Visual Basic code to an executable.
    (Compile attacker code on system. Bypass defensive counter measures.)
  command: vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb}
references: []
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
install:
- method: choco
  package_name: vbc
  commands:
  - choco install vbc
---

# vbc

vbc is a Windows LOLBin. Binary file used for compile vbs code Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe; C:\Windows\Microsoft.NET\Framework\v3.5\vbc.exe; C:\Windows\Microsoft.NET\Framework\v2.0.50727\vbc.exe.
