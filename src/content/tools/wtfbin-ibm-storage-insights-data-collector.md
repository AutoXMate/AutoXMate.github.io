---
trust_level: community
id: wtfbin-ibm-storage-insights-data-collector
namespace: wtf:bin:ibm-storage-insights-data-collector
name: IBM Storage Insights Data Collector
description: IBM creates WMI false positives
version: 1.0.0
capabilities:
- security.execution.wmi
platforms:
- windows
techniques:
- execution
execution:
  template: IBM Storage Insights Data Collector
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://www.ibm.com/support/pages/carbon-black-security-alert-executing-wmicexe
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/ibm-storage-insights-data-collector/
features:
- pipes-stdin
---

examples:
  - description: "Execute IBM Storage Insights Data Collector and observe the unusual behavior"
    command: "IBM Storage Insights Data Collector"

# IBM Storage Insights Data Collector

IBM creates WMI false positives


   
The data collector periodically runs a command like: `cmd.exe /c wmic process call create `C:\...\datacollectorbin\collectorSrvWatchDog.bat`.

This may trigger detection rules geared towards T1047: Windows Management Instrumentation which look for `wmic.exe` being used to covertly spawn processes.

*Contributed by Micah Babinski (@mbabinski), William Rotchford*
