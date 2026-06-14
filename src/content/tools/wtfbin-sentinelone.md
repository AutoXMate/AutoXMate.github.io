---
trust_level: community
id: wtfbin-sentinelone
namespace: wtf:bin:sentinelone
name: SentinelOne
description: EDRs 🤝 Malware
version: 1.0.0
capabilities:
- security.execution.powershell
platforms:
- cross-platform
techniques:
- execution
execution:
  template: SentinelOne
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/24
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/sentinelone/
features:
- interactive
- pipes-stdin
---

examples:
  - description: "Execute SentinelOne and observe the unusual behavior"
    command: "SentinelOne"

# SentinelOne

EDRs 🤝 Malware

 Encoded PowerShell


   
A legitimate PowerShell script associated with SentinelOne includes encoded PowerShell, AMSI bypass encoding, as well as strings for offensive security commands such as `Invoke-Mimikatz`. If running another security solution—like Defender—it may flag this SentinelOne legitimate PowerShell activity as malicious.

*Contributed by Dray Agha (@purp1ew0lf)*
