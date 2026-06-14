---
trust_level: community
id: wtfbin-ccm-exe
namespace: wtf:bin:ccm-exe
name: "CCM.exe (SCCM)"
description: "Windows Config Manager CCM.exe runs b64-encoded powershell"
version: "1.0.0"
capabilities:
  - security.execution.powershell
platforms:
  - windows
techniques:
  - execution
execution:
  template: "CCM.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://docs.microsoft.com/en-us/mem/configmgr/apps/deploy-use/create-deploy-scripts"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/ccm-exe/"
---
examples:
  - description: "Execute CCM.exe (SCCM) and observe the unusual behavior"
    command: "CCM.exe"

# CCM.exe (SCCM)

Windows Config Manager CCM.exe runs b64-encoded powershell.  



The commands can be large enough to take multiple Event 4104 entries.

*Contributed by mttaggart*
