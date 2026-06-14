---
id: windows-compile-csc
namespace: windows:compile:csc
name: csc
description: 'Binary file used by .NET Framework to compile C# code Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Csc.exe; C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe.'
author: Oddvar Moe
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
- csc
parameters: []
features: []
execution:
  template: csc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to the specified .exe path. (Compile attacker code on system. Bypass defensive counter measures.)
  command: csc.exe -out:{PATH:.exe} {PATH:.cs}
- description: Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to a DLL file with the same name. (Compile attacker code on system. Bypass defensive counter measures.)
  command: csc -target:library {PATH:.cs}
references:
- label: ''
  url: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_csc_susp_folder.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_execution_msbuild_started_unusal_process.toml
- type: ioc
  description: Csc.exe should normally not run as System account unless it is used for development.
install:
- method: choco
  package_name: csc
  commands:
  - choco install csc
---


# csc

csc is a Windows LOLBin. Binary file used by .NET Framework to compile C# code Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Csc.exe; C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe.
