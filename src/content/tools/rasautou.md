---
id: windows-execution-rasautou
namespace: windows:execution:rasautou
name: rasautou
description: 'Windows Remote Access Dialer Located at: C:\Windows\System32\rasautou.exe.'
author: Tony Lambert
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
- rasautou
parameters: []
features:
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: rasautou
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Loads the target .DLL specified in -d and executes the export specified
    in -p. Options removed in Windows 10. (Execute DLL code)
  command: rasautou -d {PATH:.dll} -p export_name -a a -e e
references:
- label: DueDLLigence
  url: https://github.com/fireeye/DueDLLigence
- label: staying-hidden-on-the-endpoint-evading-detection-w
  url: https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/08ca62cc8860f4660e945805d0dd615ce75258c1/rules/windows/process_creation/win_rasautou_dll_execution.yml
- type: ioc
  description: rasautou.exe command line containing -d and -p
install:
- method: choco
  package_name: rasautou
  commands:
  - choco install rasautou
---

# rasautou

rasautou is a Windows LOLBin. Windows Remote Access Dialer Located at: C:\Windows\System32\rasautou.exe.
