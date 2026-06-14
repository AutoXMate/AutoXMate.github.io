---
trust_level: community
id: wtfbin-nutanix-guest-tools
namespace: wtf:bin:nutanix-guest-tools
name: "Nutanix Guest Tools"
description: "Yet another base64-loving process"
version: "1.0.0"
capabilities:
  - security.obfuscation.base64
platforms:
  - windows
techniques:
  - defense-evasion
execution:
  template: "Nutanix Guest Tools"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/46"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/nutanix-guest-tools/"
---
examples:
  - description: "Execute Nutanix Guest Tools and observe the unusual behavior"
    command: "Nutanix Guest Tools"

# Nutanix Guest Tools

Yet another base64-loving process. 



In this case, the encoded commands are also WMI PowerShell commands.

*Contributed by Micah Babinski (@mbabinski)*
