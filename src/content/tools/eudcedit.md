---
id: windows-uacbypass-eudcedit
namespace: windows:uacbypass:eudcedit
name: eudcedit
description: 'Private Character Editor Windows Utility Located at: c:\windows\system32\eudcedit.exe;
  c:\windows\syswow64\eudcedit.exe.'
author: Matan Bahar
version: 1.0.0
capabilities:
- security.privilege-escalation.uac-bypass
platforms:
- windows
risk_level: critical
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
  - privilege_escalation
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
- eudcedit
parameters: []
features:
- pipes-stdout
- requires-root
- stealth
execution:
  template: eudcedit
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, the Private Charecter Editor will be opened - click
    OK, then click File -> Font Links. In the next window choose the option "Link
    with Selected Fonts" and click on Save As, then in the opened enter the command
    you want to execute. (Execute a binary or script as a high-integrity process without
    a UAC prompt.)
  command: eudcedit
references:
- label: windows-fonts-exploitation-in-2025-bypassing-uac-w
  url: https://medium.com/@matanb707/windows-fonts-exploitation-in-2025-bypassing-uac-with-eudcedit-915599705639
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: ioc
  description: Processes spawned by eudcedit.exe.
install:
- method: choco
  package_name: eudcedit
  commands:
  - choco install eudcedit
---

# eudcedit

eudcedit is a Windows LOLBin. Private Character Editor Windows Utility Located at: c:\windows\system32\eudcedit.exe; c:\windows\syswow64\eudcedit.exe.
