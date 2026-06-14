---
id: windows-compile-jsc
namespace: windows:compile:jsc
name: jsc
description: 'Binary file used by .NET to compile JavaScript code to .exe or .dll
  format Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Jsc.exe;
  C:\Windows\Microsoft.NET\Framework\v2.0.50727\Jsc.exe.'
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
- jsc
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: jsc
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use jsc.exe to compile JavaScript code stored in the provided .JS file
    and generate a .EXE file with the same name. (Compile attacker code on system.
    Bypass defensive counter measures.)
  command: jsc.exe {PATH:.js}
- description: Use jsc.exe to compile JavaScript code stored in the .JS file and generate
    a DLL file with the same name. (Compile attacker code on system. Bypass defensive
    counter measures.)
  command: jsc.exe /t:library {PATH:.js}
references:
- label: '998797808907046913'
  url: https://twitter.com/DissectMalware/status/998797808907046913
- label: ''
  url: https://www.phpied.com/make-your-javascript-a-windows-exe/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_lolbin_jsc.yml
- type: ioc
  description: Jsc.exe should normally not run a system unless it is used for development.
install:
- method: choco
  package_name: jsc
  commands:
  - choco install jsc
---

# jsc

jsc is a Windows LOLBin. Binary file used by .NET to compile JavaScript code to .exe or .dll format Located at: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe; C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Jsc.exe; C:\Windows\Microsoft.NET\Framework\v2.0.50727\Jsc.exe.
