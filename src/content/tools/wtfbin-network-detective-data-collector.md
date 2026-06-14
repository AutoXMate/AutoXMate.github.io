---
trust_level: community
id: wtfbin-network-detective-data-collector
namespace: wtf:bin:network-detective-data-collector
name: Network Detective Data Collector (nddc.exe)
description: WMIExec-ish NDCC
version: 1.0.0
capabilities:
- network.transfer.generic
- security.execution.impacket
platforms:
- windows
techniques:
- exfiltration
- execution
execution:
  template: Network Detective Data Collector
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/5
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/network-detective-data-collector/
features:
- network-intensive
- pipes-stdin
---

examples:
  - description: "Execute Network Detective Data Collector (nddc.exe) and observe the unusual behavior"
    command: "Network Detective Data Collector"

# Network Detective Data Collector (nddc.exe)

WMIExec-ish NDCC


   
The executable for Network Detective Data Collector displays false positive activity similar to Impacket's WMI/SMBexec.

*Contributed by Dray Agha (@purp1ew0lf)*
