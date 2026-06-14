---
trust_level: community
id: wtfbin-ringcentral-exe
namespace: wtf:bin:ringcentral-exe
name: RingCentral.exe
description: How to look like malware, by RingCentral
version: 1.0.0
capabilities:
- security.execution.script
platforms:
- windows
techniques:
- execution
execution:
  template: RingCentral.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/WidespreadPandemic/RingCentral_WTFBin
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/ringcentral-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute RingCentral.exe and observe the unusual behavior"
    command: "RingCentral.exe"

# RingCentral.exe

How to look like malware, by RingCentral


   
Binary installs deep in `AppData`, drops a `setDefaultAppByProtcol.vbs` script, that is then executed to query/create/modify registry entries by running cmd.exe to call `cscript` //NoLogo and then finally run the vbscript.

*Contributed by t3chn1qu3_/WSP (@t3chn1qu3_WSP)*
