---
trust_level: community
id: wtfbin-adobe-genuine-monitor-service
namespace: wtf:bin:adobe-genuine-monitor-service
name: "Adobe Genuine Monitor Service"
description: "A little LSASS, as a treat"
version: "1.0.0"
capabilities:
  - credential.dump.lsass
platforms:
  - windows
techniques:
  - credential-access
execution:
  template: "Adobe Genuine Monitor Service"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/17"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/adobe-genuine-monitor-service/"
---
examples:
  - description: "Execute Adobe Genuine Monitor Service and observe the unusual behavior"
    command: "Adobe Genuine Monitor Service"

# Adobe Genuine Monitor Service

A little LSASS, as a treat.


   
Adobe Genuine Monitor Service (`AGMService.exe`) opens and reads from the LSASS process. While this access is legitimate, it can create false positives for process access alerts.

*Contributed by g1ng3rr00t*
