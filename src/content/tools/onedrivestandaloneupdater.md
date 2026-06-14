---
id: windows-download-onedrivestandaloneupdater
namespace: windows:download:onedrivestandaloneupdater
name: onedrivestandaloneupdater
description: 'OneDrive Standalone Updater Located at: C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe;
  C:\Program Files\Microsoft OneDrive\OneDriveStandaloneUpdater.exe; C:\Program Files
  (x86)\Microsoft OneDrive\OneDriveStandaloneUpdater.exe.'
author: Elliot Killick
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
- onedrivestandaloneupdater
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdout
execution:
  template: onedrivestandaloneupdater
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download a file from the web address specified in `HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC`.
    `ODSUUpdateXMLUrlFromOC` and `UpdateXMLUrlFromOC` must be equal to non-empty string
    values in that same registry key. `UpdateOfficeConfigTimestamp` is a UNIX epoch
    time which must be set to a large QWORD such as 99999999999 (in decimal) to indicate
    the URL cache is good. The downloaded file will be in `%localappdata%\OneDrive\StandaloneUpdater\PreSignInSettingsConfig.json`.
    (Download a file from the Internet without executing any anomalous executables
    with suspicious arguments)
  command: OneDriveStandaloneUpdater
references:
- label: '153'
  url: https://github.com/LOLBAS-Project/LOLBAS/pull/153
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: ioc
  description: HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC
    being set to a suspicious non-Microsoft controlled URL
- type: ioc
  description: Reports of downloading from suspicious URLs in %localappdata%\OneDrive\setup\logs\StandaloneUpdate_*.log
    files
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml
install:
- method: choco
  package_name: onedrivestandaloneupdater
  commands:
  - choco install onedrivestandaloneupdater
---

# onedrivestandaloneupdater

onedrivestandaloneupdater is a Windows LOLBin. OneDrive Standalone Updater Located at: C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe; C:\Program Files\Microsoft OneDrive\OneDriveStandaloneUpdater.exe; C:\Program Files (x86)\Microsoft OneDrive\OneDriveStandaloneUpdater.exe.
