---
id: windows-execution-appcert
namespace: windows:execution:appcert
name: appcert
description: 'Windows App Certification Kit command-line tool. Located at: C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe; C:\Program Files\Windows Kits\10\App Certification Kit\appcert.exe.'
author: Avihay Eldad
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
- appcert
parameters: []
features: []
execution:
  template: appcert
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute an executable file via the Windows App Certification Kit command-line tool. (Performs execution of specified file, can be used as a defense evasion)
  command: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
- description: Install an MSI file via an msiexec instance spawned via appcert.exe as parent process. (Execute custom made MSI file with malicious code)
  command: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml}
references:
- label: using-the-windows-app-certification-kit
  url: https://learn.microsoft.com/windows/win32/win_cert/using-the-windows-app-certification-kit
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
- T1218.007
detections: []
install:
- method: choco
  package_name: appcert
  commands:
  - choco install appcert
---


# appcert

appcert is a Windows LOLBin. Windows App Certification Kit command-line tool. Located at: C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe; C:\Program Files\Windows Kits\10\App Certification Kit\appcert.exe.
