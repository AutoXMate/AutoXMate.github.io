---
id: windows-execution-msedgewebview2
namespace: windows:execution:msedgewebview2
name: msedgewebview2
description: 'msedgewebview2.exe is the executable file for Microsoft Edge WebView2, which is a web browser control used by applications to display web content. Located at: C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe; C:\Program Files (x86)\Microsoft\EdgeWebView\Application\131.0.2903.70\msedgewebview2.exe.'
author: Matan Bahar
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
- msedgewebview2
parameters: []
features: []
execution:
  template: msedgewebview2
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified executable as its subprocess. (Proxy execution of binary)
  command: msedgewebview2.exe --no-sandbox --browser-subprocess-path="{PATH_ABSOLUTE:.exe}"
- description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess. (Proxy execution of binary)
  command: msedgewebview2.exe --utility-cmd-prefix="{CMD}"
- description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess. (Proxy execution of binary)
  command: msedgewebview2.exe --disable-gpu-sandbox --gpu-launcher="{CMD}"
- description: This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess. (Proxy execution of binary)
  command: msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}"
references:
- label: one-electron-to-rule-them-all-dc2e9b263daf
  url: https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.015
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
- type: ioc
  description: 'msedgewebview2.exe spawned with any of the following: --gpu-launcher, --utility-cmd-prefix, --renderer-cmd-prefix, --browser-subprocess-path'
install:
- method: choco
  package_name: msedgewebview2
  commands:
  - choco install msedgewebview2
---


# msedgewebview2

msedgewebview2 is a Windows LOLBin. msedgewebview2.exe is the executable file for Microsoft Edge WebView2, which is a web browser control used by applications to display web content. Located at: C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe; C:\Program Files (x86)\Microsoft\EdgeWebView\Application\131.0.2903.70\msedgewebview2.exe.
