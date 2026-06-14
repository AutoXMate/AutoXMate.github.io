---
trust_level: community
id: wtfbin-jetbrains-binaries-invoke-wmi
namespace: wtf:bin:jetbrains-binaries-invoke-wmi
name: "JetBrains binaries invoke WMI"
description: "JetBrains queries security tools"
version: "1.0.0"
capabilities:
  - security.execution.wmi
platforms:
  - windows
techniques:
  - execution
execution:
  template: "JetBrains binaries invoke WMI"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://rider-support.jetbrains.com/hc/en-us/community/posts/360010724079-Why-is-Rider-making-wmic-commands-to-get-AntiVirus-name-"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/jetbrains-binaries-invoke-wmi/"
---
examples:
  - description: "Execute JetBrains binaries invoke WMI and observe the unusual behavior"
    command: "JetBrains binaries invoke WMI"

# JetBrains binaries invoke WMI

JetBrains queries security tools.


   
`idea64.exe` and `rider64.exe` from JetBrains query the installed antivirus product in the exact same way that malicious programs do using the command:

```bat
wmic /namespace:\\root\securitycenter2 path antivirusproduct get displayname,productstate
```

*Contributed by Thurein Oo*
