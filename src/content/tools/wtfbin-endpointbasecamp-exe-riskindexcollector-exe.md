---
trust_level: community
id: wtfbin-endpointbasecamp-exe-riskindexcollector-exe
namespace: wtf:bin:endpointbasecamp-exe-riskindexcollector-exe
name: EndpointBasecamp.exe, RiskIndexCollector.exe
description: A little wmic enumeration
version: 1.0.0
capabilities:
- security.execution.wmi
platforms:
- windows
techniques:
- execution
execution:
  template: EndpointBasecamp.exe, RiskIndexCollector.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://any.run/report/123b7b8262d000d098c4d18bec592f22677d2374bef1e59573a05aeea9a58b3b/73ede74d-a30d-45d2-91c2-cc1870b275f6
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/endpointbasecamp-exe-riskindexcollector-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute EndpointBasecamp.exe, RiskIndexCollector.exe and observe the unusual behavior"
    command: "EndpointBasecamp.exe, RiskIndexCollector.exe"

# EndpointBasecamp.exe, RiskIndexCollector.exe

A little wmic enumeration


   
Trend Micro `EndpointBasecamp.exe` drops `RiskIndexCollector.exe` which invoke `wmic` to get list of Hotfixes/Patches using the command `wmic qfe get Description, HotfixID, InstalledOn`

*Contributed by Thurein Oo*
