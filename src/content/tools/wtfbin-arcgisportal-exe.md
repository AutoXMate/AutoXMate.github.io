---
trust_level: community
id: wtfbin-arcgisportal-exe
namespace: wtf:bin:arcgisportal-exe
name: "ArcGISPortal.exe"
description: "Not just bad guys run `whoami`"
version: "1.0.0"
capabilities:
  - credential.discovery.whoami
platforms:
  - windows
techniques:
  - discovery
execution:
  template: "ArcGISPortal.exe"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Documentation"
    url: "https://github.com/mttaggart/wtfbins/issues/28"
  - label: "WTFBins"
    url: "https://wtfbins.netlify.app/wtfbins/arcgisportal-exe/"
---
examples:
  - description: "Execute ArcGISPortal.exe and observe the unusual behavior"
    command: "ArcGISPortal.exe"

# ArcGISPortal.exe

Not just bad guys run `whoami`.


   
`ArcGISPortal.exe` runs `whoami.exe`.
I know other Defenders have been [caught out](https://twitter.com/MikeDaniels00/status/1407383747985653769) by this weird activity. But, ArcGIS spawning whoami is completely legitimate and authorised activity. Huntress telemetry shows ~60,000 in the last 15 hours. I would advice adding this very specific activity to an ignore list, so it does not trigger a detection.

*Contributed by Dray Agha (@purp1ew0lf)*
