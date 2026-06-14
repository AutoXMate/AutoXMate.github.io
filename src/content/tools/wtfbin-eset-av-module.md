---
trust_level: community
id: wtfbin-eset-av-module
namespace: wtf:bin:eset-av-module
name: "ESET AV Module (ekrn.exe)"
description: "What is it with antivirus and weird DNS?"
version: "1.0.0"
capabilities:
  - network.exfiltration.dns
platforms:
  - windows
techniques:
  - exfiltration
execution:
  template: "ESET AV Module"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/59"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/eset-av-module/"
---
examples:
  - description: "Run the binary and monitor DNS exfiltration"
    command: "ESET AV Module"

# ESET AV Module (ekrn.exe)

What is it with antivirus and weird DNS?



ESET NOD32 Antivirus kernel (`ekrn.exe`) performs random-looking Domain Name lookups.

*Contributed by Alexandros Pappas (redblueops)*
