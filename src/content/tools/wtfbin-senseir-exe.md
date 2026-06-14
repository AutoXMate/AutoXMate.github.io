---
trust_level: community
id: wtfbin-senseir-exe
namespace: wtf:bin:senseir-exe
name: "SenseIR.exe"
description: "How much can an EDR look like malware?"
version: "1.0.0"
capabilities:
  - security.obfuscation.base64
platforms:
  - windows
techniques:
  - defense-evasion
execution:
  template: "SenseIR.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/43"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/senseir-exe/"
---
examples:
  - description: "Execute SenseIR.exe and observe the unusual behavior"
    command: "SenseIR.exe"

# SenseIR.exe

How much can an EDR look like malware?



Microsoft Defender Advanced Threat Protection uses SenseIR.exe to launch Powershell scripts that then uses .NET function `[System.IO.File]::Open()` to read another Powershell script into memory for execution. The second Powershell script executed has its parameters passed in as base64-encoded text.

*Contributed by Adam Ponce (@adamcysec)*
