---
trust_level: community
id: wtfbin-edge-chromium-browsers
namespace: wtf:bin:edge-chromium-browsers
name: Edge/Chromium Browsers
description: Bizarre sub-processes
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
- linux
techniques:
- execution
execution:
  template: Edge/Chromium Browsers
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://szeged.github.io/sprocket/architecture_overview.html#:~:text=Utility%20process%20is%20created%20right,also%20deals%20with%20extension%20extraction.
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/edge-chromium-browsers/
features:
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute Edge/Chromium Browsers and observe the unusual behavior"
    command: "Edge/Chromium Browsers"

# Edge/Chromium Browsers

Bizarre sub-processes.


   
Browsers based on Chromium will launch several sub-processes that look extremely suspicious, with command-line options like --utility and --utility-sub-type=unzip.mojom.Unzipper. Despite Google searches for these terms matching malware analysis reports, these are expected behaviors.

*Contributed by mttaggart*
