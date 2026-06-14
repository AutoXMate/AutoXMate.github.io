---
id: windows-execution-appvlp
namespace: windows:execution:appvlp
name: appvlp
description: 'Application Virtualization Utility Included with Microsoft Office 2016 Located at: C:\Program Files\Microsoft Office\root\client\appvlp.exe; C:\Program Files (x86)\Microsoft Office\root\client\appvlp.exe.'
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
- appvlp
parameters: []
features: []
execution:
  template: appvlp
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Executes .bat file through AppVLP.exe (Execution of BAT file hosted on Webdav server.)
  command: AppVLP.exe {PATH_SMB:.bat}
- description: Executes powershell.exe as a subprocess of AppVLP.exe and run the respective PS command. (Local execution of process bypassing Attack Surface Reduction (ASR).)
  command: AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)"
references:
- label: Code-Execution
  url: https://github.com/MoooKitty/Code-Execution
- label: '892388990686347264'
  url: https://twitter.com/moo_hax/status/892388990686347264
- label: ''
  url: https://enigma0x3.net/2018/06/11/the-tale-of-settingcontent-ms-files/
- label: ''
  url: https://securityboulevard.com/2018/07/attackers-test-new-document-attack-vector-that-slips-past-office-defenses/
techniques:
- execution
- defense-evasion
mitre_ids:
- T1218
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_appvlp.yml
install:
- method: choco
  package_name: appvlp
  commands:
  - choco install appvlp
---


# appvlp

appvlp is a Windows LOLBin. Application Virtualization Utility Included with Microsoft Office 2016 Located at: C:\Program Files\Microsoft Office\root\client\appvlp.exe; C:\Program Files (x86)\Microsoft Office\root\client\appvlp.exe.
