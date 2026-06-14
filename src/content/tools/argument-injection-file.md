---
trust_level: community
id: argument-injection-file
namespace: argument:injection:file
name: file
description: Argument injection via file
version: 1.0.0
capabilities:
- system.file.read
platforms:
- cross-platform
techniques:
- discovery
execution:
  template: file
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: 'Read an arbitrary file by specifying it as a magic file. This will
    result in errors containing the lines of the file. The argument parsing done by
    file also means this can be specified as a single argument. '
  command: 'file -m/etc/passwd '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/file/
features:
- file-system
- local
- stealth
---

# file

GTFOArgs entry for file. This binary can be used to inject arguments for execution, file operations, or other capabilities.
