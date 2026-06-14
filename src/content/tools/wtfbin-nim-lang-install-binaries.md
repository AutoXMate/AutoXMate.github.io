---
trust_level: community
id: wtfbin-nim-lang-install-binaries
namespace: wtf:bin:nim-lang-install-binaries
name: Nim Lang install binaries
description: The Nim language installer binaries in certain versions trigger Windows
  Defender
version: 1.0.0
capabilities:
- security.execution.nim
platforms:
- windows
techniques:
- execution
execution:
  template: Nim Lang install binaries
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/HuskyHacks/the-crown-defcon615/blob/main/notebooks/NimbleAVExcursion.ipynb
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/nim-lang-install-binaries/
features:
- pipes-stdin
---

examples:
  - description: "Execute Nim Lang install binaries and observe the unusual behavior"
    command: "Nim Lang install binaries"

# Nim Lang install binaries

The Nim language installer binaries in certain versions trigger Windows Defender. 



These include `nimble.exe`, `finish.exe`, `koch.exe`, and other binaries that come packaged during a stock install of Nim.

*Contributed by HuskyHacks*
