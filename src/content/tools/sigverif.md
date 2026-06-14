---
id: windows-execution-sigverif
namespace: windows:execution:sigverif
name: sigverif
description: 'File Signature Verification utility to verify digital signatures of
  files Located at: C:\Windows\System32\sigverif.exe; C:\Windows\SysWOW64\sigverif.exe.'
author: Moshe Kaplan
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
- sigverif
parameters: []
features:
- file-system
- local
- pipes-stdin
- pipes-stdout
execution:
  template: sigverif
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch sigverif.exe GUI, click 'Advanced', specify arbitrary executable
    path as 'log file name', then click 'View Log' to execute the binary. (Execute
    arbitrary programs through a trusted Microsoft-signed binary to bypass application
    whitelisting.)
  command: sigverif.exe
references:
- label: '1457676633809330184'
  url: https://twitter.com/0gtweet/status/1457676633809330184
- label: ''
  url: https://www.hexacorn.com/blog/2018/04/27/i-shot-the-sigverif-exe-the-gui-based-lolbin/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: ioc
  description: sigverif.exe spawning unexpected child processes
install:
- method: choco
  package_name: sigverif
  commands:
  - choco install sigverif
---

# sigverif

sigverif is a Windows LOLBin. File Signature Verification utility to verify digital signatures of files Located at: C:\Windows\System32\sigverif.exe; C:\Windows\SysWOW64\sigverif.exe.
