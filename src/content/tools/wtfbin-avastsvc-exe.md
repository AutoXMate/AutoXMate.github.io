---
trust_level: community
id: wtfbin-avastsvc-exe
namespace: wtf:bin:avastsvc-exe
name: AvastSvc.exe
description: Avast scans your network on the sly
version: 1.0.0
capabilities:
- network.tunnel.ssh
platforms:
- windows
techniques:
- command-and-control
execution:
  template: AvastSvc.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/38
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/avastsvc-exe/
features:
- network-intensive
---

examples:
  - description: "Execute AvastSvc.exe and observe the unusual behavior"
    command: "AvastSvc.exe"

# AvastSvc.exe

Avast scans your network on the sly.


   
During scans, `AvastSvc.exe` will attempt to connect to neighboring IP addresses over SSH. Users such as `FakeDomain\FakeUser` will be used, as well as blank users/null SIDs.

*Contributed by mttaggart*
