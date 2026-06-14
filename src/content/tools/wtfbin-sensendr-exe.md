---
trust_level: community
id: wtfbin-sensendr-exe
namespace: wtf:bin:sensendr-exe
name: "SenseNdr.exe"
description: "SenseNDR base64 encoding"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - windows
techniques:
  - execution
execution:
  template: "SenseNdr.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/20"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/sensendr-exe/"
---
examples:
  - description: "Execute SenseNdr.exe and observe the unusual behavior"
    command: "SenseNdr.exe"

# SenseNdr.exe

SenseNDR base64 encoding


   
SenseNDR, a component of [Microsoft Defender for Endpoint](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/device-discovery?view=o365-worldwide), encodes data for transmission in massive base64 chunks.

*Contributed by Bumbucha*
