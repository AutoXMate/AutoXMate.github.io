---
id: windows-download-printbrm
namespace: windows:download:printbrm
name: printbrm
description: 'Printer Migration Command-Line Tool Located at: C:\Windows\System32\spool\tools\PrintBrm.exe.'
author: Elliot Killick
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.alternate-data-stream
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
  - filesystem_write
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
- printbrm
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- streaming
execution:
  template: printbrm
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Create a ZIP file from a folder in a remote drive (Exfiltrate the contents
    of a remote folder on a UNC share into a zip file)
  command: PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip}
- description: Extract the contents of a ZIP file stored in an Alternate Data Stream
    (ADS) and store it in a folder (Decompress and extract a ZIP file stored on an
    alternate data stream to a new folder)
  command: PrintBrm -r -f {PATH_ABSOLUTE}:hidden.zip -d {PATH_ABSOLUTE:folder}
references:
- label: '1404117015447670800'
  url: https://twitter.com/elliotkillick/status/1404117015447670800
techniques:
- exfiltration
- defense-evasion
mitre_ids:
- T1105
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml
- type: ioc
  description: PrintBrm.exe should not be run on a normal workstation
install:
- method: choco
  package_name: printbrm
  commands:
  - choco install printbrm
---

# printbrm

printbrm is a Windows LOLBin. Printer Migration Command-Line Tool Located at: C:\Windows\System32\spool\tools\PrintBrm.exe.
