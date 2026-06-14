---
id: windows-bypass-visualuiaverifynative
namespace: windows:bypass:visualuiaverifynative
name: visualuiaverifynative
description: 'A Windows SDK binary for manual and automated testing of Microsoft UI
  Automation implementation and controls. Located at: c:\Program Files (x86)\Windows
  Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe; c:\Program Files
  (x86)\Windows Kits\10\bin\<version>\x64\UIAVerify\VisualUiaVerifyNative.exe; c:\Program
  Files (x86)\Windows Kits\10\bin\<version>\UIAVerify\VisualUiaVerifyNative.exe.'
author: Jimmy (@bohops)
version: 1.0.0
capabilities:
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
- visualuiaverifynative
parameters: []
features:
- file-system
- local
- pipes-stdout
- stealth
execution:
  template: visualuiaverifynative
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Generate Serialized gadget and save to - `C:\Users\%USERNAME%\AppData\Roaminguiverify.config`
    before executing. (Execute proxied payload with Microsoft signed binary to bypass
    WDAC policies)
  command: VisualUiaVerifyNative.exe
references:
- label: ''
  url: https://bohops.com/2020/10/15/exploring-the-wdac-microsoft-recommended-block-rules-visualuiaverifynative/
- label: 937db704b9148e9cee7c7010cad4d00ce9c4fdad
  url: https://github.com/MicrosoftDocs/windows-itpro-docs/commit/937db704b9148e9cee7c7010cad4d00ce9c4fdad
techniques:
- defense-evasion
mitre_ids:
- T1218
detections:
- type: blockrule
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- type: sigma
  url: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml
- type: ioc
  description: As a Windows SDK binary, execution on a system may be suspicious
install:
- method: choco
  package_name: visualuiaverifynative
  commands:
  - choco install visualuiaverifynative
---

# visualuiaverifynative

visualuiaverifynative is a Windows LOLBin. A Windows SDK binary for manual and automated testing of Microsoft UI Automation implementation and controls. Located at: c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe; c:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\UIAVerify\VisualUiaVerifyNative.exe; c:\Program Files (x86)\Windows Kits\10\bin\<version>\UIAVerify\VisualUiaVerifyNative.exe.
