---
trust_level: community
id: argument-injection-gcc
namespace: argument:injection:gcc
name: gcc
description: "Argument injection via gcc"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "gcc"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The `-wrapper` argument invokes all subcommands under a wrapper program."
    command: "gcc -wrapper /bin/sh,-s .
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/gcc/"
---

# gcc

GTFOArgs entry for gcc. This binary can be used to inject arguments for execution, file operations, or other capabilities.
