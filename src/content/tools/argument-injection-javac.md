---
trust_level: community
id: argument-injection-javac
namespace: argument:injection:javac
name: javac
description: Argument injection via javac
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- cross-platform
techniques:
- execution
execution:
  template: javac
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to execute already-compiled Java code. `malicious-agent`
    is a local file which has somehow found its way onto the server that `javac` is
    running, and is a compiled Java runtime. See [DU_CTF2022](https://github.com/DownUnderCTF/Challenges_2022_Public/tree/main/web/university-of-straya-part1/solution)
    for more information about this.
  command: 'javac -d output.jar -J-malicious-agent '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/javac/
features:
- pipes-stdin
- stealth
---

# javac

GTFOArgs entry for javac. This binary can be used to inject arguments for execution, file operations, or other capabilities.
