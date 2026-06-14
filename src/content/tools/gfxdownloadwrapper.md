---
id: windows-download-gfxdownloadwrapper
namespace: windows:download:gfxdownloadwrapper
name: gfxdownloadwrapper
description: 'Remote file download used by the Intel Graphics Control Panel, receives
  as first parameter a URL and a destination file path. Located at: c:\windows\system32\driverstore\filerepository\64kb6472.inf_amd64_3daef03bbe98572b\GfxDownloadWrapper.exe;
  c:\windows\system32\driverstore\filerepository\cui_comp.inf_amd64_0e9c57ae3396e055\GfxDownloadWrapper.exe;
  c:\windows\system32\driverstore\filerepository\cui_comp.inf_amd64_209bd95d56b1ac2d\GfxDownloadWrapper.exe.'
author: Jesus Galvez
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
- gfxdownloadwrapper
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: gfxdownloadwrapper
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: GfxDownloadWrapper.exe downloads the content that returns URL and writes
    it to the file DESTINATION FILE PATH. The binary is signed by "Microsoft Windows
    Hardware", "Compatibility Publisher", "Microsoft Windows Third Party Component
    CA 2012", "Microsoft Time-Stamp PCA 2010", "Microsoft Time-Stamp Service". (Download
    file from internet)
  command: C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe
    "URL" "DESTINATION FILE"
references:
- label: ''
  url: https://www.sothis.tech/author/jgalvez/
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_gfxdownloadwrapper_file_download.yml
- type: ioc
  description: Usually GfxDownloadWrapper downloads a JSON file from https://gameplayapi.intel.com.
install:
- method: choco
  package_name: gfxdownloadwrapper
  commands:
  - choco install gfxdownloadwrapper
---

# gfxdownloadwrapper

gfxdownloadwrapper is a Windows LOLBin. Remote file download used by the Intel Graphics Control Panel, receives as first parameter a URL and a destination file path. Located at: c:\windows\system32\driverstore\filerepository\64kb6472.inf_amd64_3daef03bbe98572b\GfxDownloadWrapper.exe; c:\windows\system32\driverstore\filerepository\cui_comp.inf_amd64_0e9c57ae3396e055\GfxDownloadWrapper.exe; c:\windows\system32\driverstore\filerepository\cui_comp.inf_amd64_209bd95d56b1ac2d\GfxDownloadWrapper.exe.
