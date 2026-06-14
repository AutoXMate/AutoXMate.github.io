---
trust_level: community
id: wtfbin-ibm-s-pcsnp-exe-triggers-system-cmd-exe
namespace: wtf:bin:ibm-s-pcsnp-exe-triggers-system-cmd-exe
name: IBM's pcsnp.exe triggers SYSTEM cmd.exe
description: IBM's `pcsnp.exe` just...what
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: IBM's pcsnp.exe triggers SYSTEM cmd.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/58
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/ibm-s-pcsnp-exe-triggers-system-cmd-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute IBM's pcsnp.exe triggers SYSTEM cmd.exe and observe the unusual behavior"
    command: "IBM's pcsnp.exe triggers SYSTEM cmd.exe"

# IBM's pcsnp.exe triggers SYSTEM cmd.exe

IBM's `pcsnp.exe` just...what


   
IBM's `pcsnp.exe` calls `cmd.exe /c mkdir C:\Temp` from processes such as `mpnotify.exe` and `lsass.exe`. Read the writeup for this; it's amazing.

*Contributed by 59e5aaf4*
