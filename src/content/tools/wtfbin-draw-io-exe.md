---
trust_level: community
id: wtfbin-draw-io-exe
namespace: wtf:bin:draw-io-exe
name: draw.io.exe
description: Nothing to see here
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: draw.io.exe
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/53
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/draw-io-exe/
features:
- pipes-stdin
---

examples:
  - description: "Execute draw.io.exe and observe the unusual behavior"
    command: "draw.io.exe"

# draw.io.exe

Nothing to see here


   
`draw.io.exe` uses `attrib.exe` to hide the file `.dtmp` using the command `attrib +h filename.dtmp.`

*Contributed by Thurein Oo*
