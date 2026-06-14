---
trust_level: community
id: wtfbin-noregon-fake-windows-components
namespace: wtf:bin:noregon-fake-windows-components
name: Noregon Fake Windows Components
description: Named after legitimate Windows binaries, in the wrong location
version: 1.0.0
capabilities:
- security.defenseevasion.masquerading
platforms:
- windows
techniques:
- defense-evasion
execution:
  template: Noregon Fake Windows Components
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/16
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/noregon-fake-windows-components/
features:
- pipes-stdout
---

examples:
  - description: "Execute Noregon Fake Windows Components and observe the unusual behavior"
    command: "Noregon Fake Windows Components"

# Noregon Fake Windows Components

Named after legitimate Windows binaries, in the wrong location. 



They were spawned in succession from `C:\Program Files (x86)\noregon\JPRO diagnostics\Fleets.exe` > `C:\Program Files (x86)\noregon\JPRO diagnostics_jpro_start.exe` > `C:\Users\AppData\Local\icsys.icn.exe > c:\Windows\System\explorer.exe` > `C:\Windows\System\spoolsv.exe` > `C:\Windows\System\svchost.exe`.

The files are custom binaries compiled with Visual Basic. They appear to be changed/created regularly as the hashes seem to change often.

*Contributed by Matt Anderson*
