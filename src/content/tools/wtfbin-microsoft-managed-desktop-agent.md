---
trust_level: community
id: wtfbin-microsoft-managed-desktop-agent
namespace: wtf:bin:microsoft-managed-desktop-agent
name: "Microsoft Managed Desktop Agent"
description: "Microsoft loves to look like malware, huh?"
version: "1.0.0"
capabilities:
  - security.execution.powershell
platforms:
  - windows
techniques:
  - execution
execution:
  template: "Microsoft Managed Desktop Agent"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/60"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/microsoft-managed-desktop-agent/"
---
examples:
  - description: "Execute Microsoft Managed Desktop Agent and observe the unusual behavior"
    command: "Microsoft Managed Desktop Agent"

# Microsoft Managed Desktop Agent

Microsoft loves to look like malware, huh?



[Microsoft Management Services Cloud Managed Desktop Agent](https://learn.microsoft.com/en-us/managed-desktop/overview/service-plan) runs b64 PowerShell.

*Contributed by Alexandros Pappas (redblueops)*
