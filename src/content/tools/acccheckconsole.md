---
id: windows-execution-acccheckconsole
namespace: windows:execution:acccheckconsole
name: acccheckconsole
description: 'Verifies UI accessibility requirements Located at: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\AccChecker\AccCheckConsole.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm\AccChecker\AccCheckConsole.exe.'
author: bohops
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
- acccheckconsole
parameters: []
features: []
execution:
  template: acccheckconsole
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name. (Local execution of managed code from assembly DLL.)
  command: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
- description: Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name. (Local execution of managed code to bypass AppLocker.)
  command: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
references:
- label: 2444129419c8acf837aedda5f0e7f340
  url: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
- label: '1477717351017680899'
  url: https://twitter.com/bohops/status/1477717351017680899
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_susp_acccheckconsole.yml
- type: ioc
  description: Sysmon Event ID 1 - Process Creation
- type: other
  url: https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
install:
- method: choco
  package_name: acccheckconsole
  commands:
  - choco install acccheckconsole
---


# acccheckconsole

acccheckconsole is a Windows LOLBin. Verifies UI accessibility requirements Located at: C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\AccChecker\AccCheckConsole.exe; C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\arm\AccChecker\AccCheckConsole.exe.
