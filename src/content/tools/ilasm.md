---
id: windows-compile-ilasm
namespace: windows:compile:ilasm
name: ilasm
description: 'used for compile c# code into dll or exe. Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe;
  C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ilasm.exe.'
author: Hai vaknin (lux)
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
- ilasm
parameters: []
features:
- pipes-stdin
- pipes-stdout
execution:
  template: ilasm
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Binary file used by .NET to compile C#/intermediate (IL) code to .exe
    (Compile attacker code on system. Bypass defensive counter measures.)
  command: ilasm.exe {PATH_ABSOLUTE:.txt} /exe
- description: Binary file used by .NET to compile C#/intermediate (IL) code to dll
    (A description of the usecase)
  command: ilasm.exe {PATH_ABSOLUTE:.txt} /dll
references:
- label: hello_world.txt
  url: https://github.com/LuxNoBulIshit/BeforeCompileBy-ilasm/blob/master/hello_world.txt
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: ioc
  description: Ilasm may not be used often in production environments (such as on
    endpoints)
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ilasm.yml
install:
- method: choco
  package_name: ilasm
  commands:
  - choco install ilasm
---

# ilasm

ilasm is a Windows LOLBin. used for compile c# code into dll or exe. Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ilasm.exe.
