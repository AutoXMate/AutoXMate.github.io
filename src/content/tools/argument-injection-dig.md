---
trust_level: community
id: argument-injection-dig
namespace: argument:injection:dig
name: dig
description: "Argument injection via dig"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - cross-platform
techniques:
  - discovery
execution:
  template: "dig"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Read an arbitrary file by specifying it as a batch file. Note that this will leak lines of the file read as outbound DNS lookups."
    command: "dig -f /etc/passwd
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/dig/"
---

# dig

GTFOArgs entry for dig. This binary can be used to inject arguments for execution, file operations, or other capabilities.
