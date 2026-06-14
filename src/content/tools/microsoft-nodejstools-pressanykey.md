---
id: windows-execution-microsoft-nodejstools-pressanykey
namespace: windows:execution:microsoft-nodejstools-pressanykey
name: microsoft-nodejstools-pressanykey
description: 'Part of the NodeJS Visual Studio tools. Located at: C:\Program Files\Microsoft
  Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe;
  C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe.'
author: mr.d0x
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
- microsoft-nodejstools-pressanykey
parameters: []
features:
- file-system
- interactive
- local
- pipes-stdin
- pipes-stdout
execution:
  template: microsoft-nodejstools-pressanykey
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Launch specified executable as a subprocess of Microsoft.NodejsTools.PressAnyKey.exe.
    (Spawn a new process via Microsoft.NodejsTools.PressAnyKey.exe.)
  command: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe}
references:
- label: '1463526834918854661'
  url: https://twitter.com/mrd0x/status/1463526834918854661
techniques:
- execution
- defense-evasion
mitre_ids:
- T1127
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml
install:
- method: choco
  package_name: microsoft-nodejstools-pressanykey
  commands:
  - choco install microsoft-nodejstools-pressanykey
---

# microsoft-nodejstools-pressanykey

microsoft-nodejstools-pressanykey is a Windows LOLBin. Part of the NodeJS Visual Studio tools. Located at: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe; C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe.
