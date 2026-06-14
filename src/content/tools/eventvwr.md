---
id: windows-uacbypass-eventvwr
namespace: windows:uacbypass:eventvwr
name: eventvwr
description: 'Displays Windows Event Logs in a GUI window. Located at: C:\Windows\System32\eventvwr.exe; C:\Windows\SysWOW64\eventvwr.exe.'
author: Jacob Gajek
version: 1.0.0
capabilities:
- security.privilege-escalation.uac-bypass
platforms:
- windows
risk_level: critical
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
  - privilege_escalation
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
- eventvwr
parameters: []
features: []
execution:
  template: eventvwr
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: During startup, eventvwr.exe checks the registry value `HKCU\Software\Classes\mscfile\shell\open\command` for the location of mmc.exe, which is used to open the eventvwr.msc saved console file. If the location of another binary or script is added to this registry value, it will be executed as a high-integrity process without a UAC prompt being displayed to the user. (Execute a binary or script as a high-integrity process without a UAC prompt.)
  command: eventvwr.exe
- description: During startup, eventvwr.exe uses .NET deserialization with `%LOCALAPPDATA%\Microsoft\EventV~1\RecentViews` file. This file can be created using https://github.com/pwntester/ysoserial.net (Execute a command to bypass security restrictions that limit the use of command-line interpreters.)
  command: ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews & eventvwr.exe
references:
- label: ''
  url: https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- label: Invoke-EventVwrBypass.ps1
  url: https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-EventVwrBypass.ps1
- label: '1518970259868626944'
  url: https://twitter.com/orange_8361/status/1518970259868626944
techniques:
- privilege-escalation
mitre_ids:
- T1548.002
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/d31ea6253ea40789b1fc49ade79b7ec92154d12a/rules/windows/privilege_escalation_uac_bypass_event_viewer.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/eventvwr_uac_bypass.yml
- type: ioc
  description: eventvwr.exe launching child process other than mmc.exe
- type: ioc
  description: Creation or modification of the registry value HKCU\Software\Classes\mscfile\shell\open\command
install:
- method: choco
  package_name: eventvwr
  commands:
  - choco install eventvwr
---


# eventvwr

eventvwr is a Windows LOLBin. Displays Windows Event Logs in a GUI window. Located at: C:\Windows\System32\eventvwr.exe; C:\Windows\SysWOW64\eventvwr.exe.
