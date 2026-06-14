---
trust_level: community
id: wtfbin-logmein-and-cscript
namespace: wtf:bin:logmein-and-cscript
name: LogMeIn and CScript
description: Who doesn't love CScript?
version: 1.0.0
capabilities:
- security.execution.script
platforms:
- windows
techniques:
- execution
execution:
  template: LogMeIn and CScript
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://community.logmein.com/t5/LogMeIn-Central-Discussions/Why-AVfilter-js-running-in-my-logMein-client-machines/td-p/255466
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/logmein-and-cscript/
features:
- pipes-stdin
---

examples:
  - description: "Execute LogMeIn and CScript and observe the unusual behavior"
    command: "LogMeIn and CScript"

# LogMeIn and CScript

Who doesn't love CScript?


   
LogMeIn runs `avfilter.js` via `cscript` to check what AV is running on your system for some godawful reason. As far as I am aware, they have yet to provide any substantial documentation or reasoning as to why.

*Contributed by t3chn1qu3_/WSP (@t3chn1qu3_WSP)*
