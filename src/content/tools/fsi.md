---
id: windows-bypass-fsi
namespace: windows:bypass:fsi
name: fsi
description: '64-bit FSharp (F#) Interpreter included with Visual Studio and DotNet
  Core SDK. Located at: C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe; C:\Program
  Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsi.exe.'
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
- fsi
parameters: []
features:
- file-system
- local
- pipes-stdout
- stealth
execution:
  template: fsi
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute F# code via script file (Execute payload with Microsoft signed
    binary to bypass WDAC policies)
  command: fsi.exe {PATH:.fsscript}
- description: Execute F# code via interactive command line (Execute payload with
    Microsoft signed binary to bypass WDAC policies)
  command: fsi.exe
references:
- label: '904273264385589248'
  url: https://twitter.com/NickTyrer/status/904273264385589248
- label: ''
  url: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
techniques:
- defense-evasion
- execution
mitre_ids:
- T1059
detections:
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Fsi.exe execution may be suspicious on non-developer machines
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
install:
- method: choco
  package_name: fsi
  commands:
  - choco install fsi
---

# fsi

fsi is a Windows LOLBin. 64-bit FSharp (F#) Interpreter included with Visual Studio and DotNet Core SDK. Located at: C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe; C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsi.exe.
