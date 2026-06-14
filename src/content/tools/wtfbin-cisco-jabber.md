---
trust_level: community
id: wtfbin-cisco-jabber
namespace: wtf:bin:cisco-jabber
name: "Cisco Jabber"
description: "Cisco enumerates your system"
version: "1.0.0"
capabilities:
  - system.file.write
platforms:
  - windows
techniques:
  - impact
execution:
  template: "Cisco Jabber"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/45"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/cisco-jabber/"
---
examples:
  - description: "Execute Cisco Jabber and observe the unusual behavior"
    command: "Cisco Jabber"

# Cisco Jabber

Cisco enumerates your system.


   
`CiscoJabberPrt.exe` will pipe `ipconfig.exe /all`, `systeminfo.exe`, and `tasklist.exe` into a file named `Systeminfo.txt` inside of the User's `%TEMP%` folder.

*Contributed by Alex Walston (@4ayymm)*
