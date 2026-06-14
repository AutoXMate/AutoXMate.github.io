---
trust_level: community
id: wtfbin-adobe-cc-setup
namespace: wtf:bin:adobe-cc-setup
name: Adobe CC Setup
description: Adobe performs...process injection??
version: 1.0.0
capabilities:
- security.defenseevasion.process-injection
platforms:
- windows
techniques:
- defense-evasion
execution:
  template: Adobe CC Setup
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/71
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/adobe-cc-setup/
features:
- file-system
- process-manip
- stealth
---

examples:
  - description: "Execute Adobe CC Setup and observe the unusual behavior"
    command: "Adobe CC Setup"

# Adobe CC Setup

Adobe performs...process injection??



Adobe Creative Cloud setup spawns and injects code to explorer.exe for deleting itself. The injected function calls `WaitForSingleObject(INFINITE)` on the injector's process duplicated handle, then `CloseHandle` it, follows to loop over `DeleteFileW` to retry while it fails with an inner `Sleep(1000)` until success, then calls `ExitProcess(0)`.

*Contributed by Freddy Ouzan (@falsneg), John Harrison (@Cratez)*
