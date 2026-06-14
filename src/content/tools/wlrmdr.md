---
id: windows-execution-wlrmdr
namespace: windows:execution:wlrmdr
name: wlrmdr
description: 'Windows Logon Reminder executable Located at: c:\windows\system32\wlrmdr.exe.'
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
- wlrmdr
parameters: []
features:
- file-system
- pipes-stdin
- pipes-stdout
execution:
  template: wlrmdr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute executable with wlrmdr.exe as parent process (Use wlrmdr as
    a proxy binary to evade defensive countermeasures)
  command: wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe}
references:
- label: '1493963591745220608'
  url: https://twitter.com/0gtweet/status/1493963591745220608
- label: '927437787242090496'
  url: https://twitter.com/Oddvarmoe/status/927437787242090496
- label: '1461625526640992260'
  url: https://twitter.com/falsneg/status/1461625526640992260
- label: ns-shellapi-notifyicondataw
  url: https://docs.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataw
techniques:
- execution
- defense-evasion
mitre_ids:
- T1202
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wlrmdr.yml
- type: ioc
  description: wlrmdr.exe spawning any new processes
install:
- method: choco
  package_name: wlrmdr
  commands:
  - choco install wlrmdr
---

# wlrmdr

wlrmdr is a Windows LOLBin. Windows Logon Reminder executable Located at: c:\windows\system32\wlrmdr.exe.
