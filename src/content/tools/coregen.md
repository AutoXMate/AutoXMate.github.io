---
id: windows-execution-coregen
namespace: windows:execution:coregen
name: coregen
description: 'Binary coregen.exe (Microsoft CoreCLR Native Image Generator) loads exported function GetCLRRuntimeHost from coreclr.dll or from .DLL in arbitrary path. Coregen is located within "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\" or another version of Silverlight. Coregen is signed by Microsoft and bundled with Microsoft Silverlight. Located at: C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe; C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\coregen.exe.'
author: Martin Sohn Christensen
version: 1.0.0
capabilities:
- security.execution.command
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
- coregen
parameters: []
features: []
execution:
  template: coregen
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads the target .DLL in arbitrary path specified with /L. (Execute DLL code)
  command: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
- description: Loads the coreclr.dll in the corgen.exe directory (e.g. C:\Program Files\Microsoft Silverlight\5.1.50918.0). (Execute DLL code)
  command: coregen.exe dummy_assembly_name
- description: Loads the target .DLL in arbitrary path specified with /L. Since binary is signed it can also be used to bypass application whitelisting solutions. (Execute DLL code)
  command: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
references:
- label: watch?v=75XImxOOInU
  url: https://www.youtube.com/watch?v=75XImxOOInU
- label: staying-hidden-on-the-endpoint-evading-detection-w
  url: https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1055
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/image_load/image_load_side_load_coregen.yml
- type: ioc
  description: coregen.exe loading .dll file not in "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\"
- type: ioc
  description: coregen.exe loading .dll file not named coreclr.dll
- type: ioc
  description: coregen.exe command line containing -L or -l
- type: ioc
  description: coregen.exe command line containing unexpected/invald assembly name
- type: ioc
  description: coregen.exe application crash by invalid assembly name
install:
- method: choco
  package_name: coregen
  commands:
  - choco install coregen
---


# coregen

coregen is a Windows LOLBin. Binary coregen.exe (Microsoft CoreCLR Native Image Generator) loads exported function GetCLRRuntimeHost from coreclr.dll or from .DLL in arbitrary path. Coregen is located within "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\" or another version of Silverlight. Coregen is signed by Microsoft and bundled with Microsoft Silverlight. Located at: C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe; C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\coregen.exe.
