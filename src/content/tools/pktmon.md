---
id: windows-recon-pktmon
namespace: windows:recon:pktmon
name: pktmon
description: 'Capture Network Packets on the windows 10 with October 2018 Update or later. Located at: c:\windows\system32\pktmon.exe; c:\windows\syswow64\pktmon.exe.'
author: Derek Johnson
version: 1.0.0
capabilities:
- recon.enumeration
platforms:
- windows
risk_level: low
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
- pktmon
parameters: []
features: []
execution:
  template: pktmon
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Will start a packet capture and store log file as PktMon.etl. Use pktmon.exe stop (use this a built in network sniffer on windows 10 to capture senstive traffic)
  command: pktmon.exe start --etw
- description: Select Desired ports for packet capture (Look for interesting traffic such as telent or FTP)
  command: pktmon.exe filter add -p 445
references:
- label: ''
  url: https://binar-x79.com/windows-10-secret-sniffer/
techniques:
- discovery
mitre_ids:
- T1040
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_pktmon.yml
- type: ioc
  description: .etl files found on system
install:
- method: choco
  package_name: pktmon
  commands:
  - choco install pktmon
---


# pktmon

pktmon is a Windows LOLBin. Capture Network Packets on the windows 10 with October 2018 Update or later. Located at: c:\windows\system32\pktmon.exe; c:\windows\syswow64\pktmon.exe.
