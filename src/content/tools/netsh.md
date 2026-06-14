---
id: windows-execution-netsh
namespace: windows:execution:netsh
name: netsh
description: 'Netsh is a Windows tool used to manipulate network interface settings. Located at: C:\WINDOWS\System32\Netsh.exe; C:\WINDOWS\SysWOW64\Netsh.exe.'
author: Freddie Barr-Smith
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
- netsh
parameters: []
features: []
execution:
  template: netsh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Use Netsh in order to execute a .dll file and also gain persistence, every time the netsh command is called (Proxy execution of .dll)
  command: netsh.exe add helper {PATH_ABSOLUTE:.dll}
references:
- label: trix.html
  url: https://freddiebarrsmith.com/trix/trix.html
- label: netshell.html
  url: https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html
- label: ''
  url: https://liberty-shell.com/sec/2018/07/28/netshlep/
techniques:
- execution
- persistence
mitre_ids:
- T1546.007
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/processes_launching_netsh.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/deprecated/processes_created_by_netsh.yml
- type: ioc
  description: Netsh initiating a network connection
install:
- method: choco
  package_name: netsh
  commands:
  - choco install netsh
---


# netsh

netsh is a Windows LOLBin. Netsh is a Windows tool used to manipulate network interface settings. Located at: C:\WINDOWS\System32\Netsh.exe; C:\WINDOWS\SysWOW64\Netsh.exe.
