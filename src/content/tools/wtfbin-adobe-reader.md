---
trust_level: community
id: wtfbin-adobe-reader
namespace: wtf:bin:adobe-reader
name: Adobe Reader (reader_sl.exe)
description: Adobe Reader for no reason starts a subprocess using the command line
  "I run"
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- windows
techniques:
- execution
execution:
  template: Adobe Reader
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/7
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/adobe-reader/
features:
- compression
- file-system
- pipes-stdin
- process-manip
---

examples:
  - description: "Execute Adobe Reader (reader_sl.exe) and observe the unusual behavior"
    command: "Adobe Reader"

# Adobe Reader (reader_sl.exe)

Adobe Reader for no reason starts a subprocess using the command line "I run".

*Contributed by 59e5aaf4*
