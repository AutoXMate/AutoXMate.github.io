---
trust_level: community
id: wtfbin-startupscan-dll
namespace: wtf:bin:startupscan-dll
name: "Startupscan.dll"
description: "Windows being sus? Inconceivable!"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
execution:
  template: "Startupscan.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/49"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/startupscan-dll/"
---
examples:
  - description: "Execute Startupscan.dll and observe the unusual behavior"
    command: "Startupscan.dll"

# Startupscan.dll

Windows being sus? Inconceivable!



Windows executes a suspiciously named DLL export with a name of `SusRunTask`, and this DLL checks many various Scheduled Task and Autostart execution locations, such as Registry persistence locations and `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\`, as well as spawning new processes that are not child processes.

*Contributed by Matthew W (@0xDeadcell)*
