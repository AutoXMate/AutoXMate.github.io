---
id: windows-download-cmdl32
namespace: windows:download:cmdl32
name: cmdl32
description: 'Microsoft Connection Manager Auto-Download Located at: C:\Windows\System32\cmdl32.exe;
  C:\Windows\SysWOW64\cmdl32.exe.'
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
- cmdl32
parameters: []
features:
- network-intensive
- pipes-stdout
- remote
execution:
  template: cmdl32
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download a file from the web address specified in the configuration
    file. The downloaded file will be in %TMP% under the name VPNXXXX.tmp where "X"
    denotes a random number or letter. (Download file from Internet)
  command: cmdl32 /vpn /lan %cd%\config
references:
- label: '151'
  url: https://github.com/LOLBAS-Project/LOLBAS/pull/151
- label: '1455897435063074824'
  url: https://twitter.com/ElliotKillick/status/1455897435063074824
- label: ''
  url: https://elliotonsecurity.com/living-off-the-land-reverse-engineering-methodology-plus-tips-and-tricks-cmdl32-case-study/
techniques:
- exfiltration
mitre_ids:
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_cmdl32.yml
- type: ioc
  description: Reports of downloading from suspicious URLs in %TMP%\config.log
- type: ioc
  description: Useragent Microsoft(R) Connection Manager Vpn File Update
install:
- method: choco
  package_name: cmdl32
  commands:
  - choco install cmdl32
---

# cmdl32

cmdl32 is a Windows LOLBin. Microsoft Connection Manager Auto-Download Located at: C:\Windows\System32\cmdl32.exe; C:\Windows\SysWOW64\cmdl32.exe.
