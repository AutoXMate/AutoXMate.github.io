---
trust_level: community
id: wtfbin-securityhealthservice-exe-unprotects-lsa
namespace: wtf:bin:securityhealthservice-exe-unprotects-lsa
name: "SecurityHealthService.exe unprotects LSA"
description: "Who needs protection? Not LSA!"
version: "1.0.0"
capabilities:
  - credential.dump.lsass
platforms:
  - windows
techniques:
  - credential-access
execution:
  template: "SecurityHealthService.exe unprotects LSA"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/44"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/securityhealthservice-exe-unprotects-lsa/"
---
examples:
  - description: "Execute SecurityHealthService.exe unprotects LSA and observe the unusual behavior"
    command: "SecurityHealthService.exe unprotects LSA"

# SecurityHealthService.exe unprotects LSA

Who needs protection? Not LSA!


   
Sets `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL` to 0 (= insecure = might raise EDR alerts ahem ahem) just before setting it (back?) to 2 for no valid reason.

*Contributed by 59e5aaf4*
