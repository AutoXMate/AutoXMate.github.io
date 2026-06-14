---
id: windows-uacbypass-computerdefaults
namespace: windows:uacbypass:computerdefaults
name: computerdefaults
description: 'ComputerDefaults.exe is a Windows system utility for managing default
  applications for tasks like web browsing, emailing, and media playback. Located
  at: C:\Windows\System32\ComputerDefaults.exe; C:\Windows\SysWOW64\ComputerDefaults.exe.'
author: Eron Clarke
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
- computerdefaults
parameters: []
features:
- pipes-stdout
- requires-root
- stealth
execution:
  template: computerdefaults
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Upon execution, ComputerDefaults.exe checks two registry values at
    HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command; if these are
    set by an attacker, the set command will be executed as a high-integrity process
    without a UAC prompt being displayed to the user. See 'resources' for which registry
    keys/values to set. (Execute a binary or script as a high-integrity process without
    a UAC prompt.)
  command: ComputerDefaults.exe
references:
- label: 812547525107bd138a1a839118a3a44b
  url: https://gist.github.com/havoc3-3/812547525107bd138a1a839118a3a44b
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: ioc
  description: Event ID 10
- type: ioc
  description: A binary or script spawned as a child process of ComputerDefaults.exe
- type: ioc
  description: Changes to HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml
install:
- method: choco
  package_name: computerdefaults
  commands:
  - choco install computerdefaults
---

# computerdefaults

computerdefaults is a Windows LOLBin. ComputerDefaults.exe is a Windows system utility for managing default applications for tasks like web browsing, emailing, and media playback. Located at: C:\Windows\System32\ComputerDefaults.exe; C:\Windows\SysWOW64\ComputerDefaults.exe.
