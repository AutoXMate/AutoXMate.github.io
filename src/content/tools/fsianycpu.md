---
id: windows-bypass-fsianycpu
namespace: windows:bypass:fsianycpu
name: fsianycpu
description: '32/64-bit FSharp (F#) Interpreter included with Visual Studio. Located
  at: c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe.'
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
- fsianycpu
parameters: []
features:
- file-system
- local
- pipes-stdout
- stealth
execution:
  template: fsianycpu
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute F# code via script file (Execute payload with Microsoft signed
    binary to bypass WDAC policies)
  command: fsianycpu.exe {PATH:.fsscript}
- description: Execute F# code via interactive command line (Execute payload with
    Microsoft signed binary to bypass WDAC policies)
  command: fsianycpu.exe
references:
- label: ''
  url: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
techniques:
- defense-evasion
- execution
mitre_ids:
- T1059
detections:
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: FsiAnyCpu.exe execution may be suspicious on non-developer machines
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
install:
- method: choco
  package_name: fsianycpu
  commands:
  - choco install fsianycpu
---

# fsianycpu

fsianycpu is a Windows LOLBin. 32/64-bit FSharp (F#) Interpreter included with Visual Studio. Located at: c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe.
