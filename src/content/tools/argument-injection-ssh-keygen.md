---
trust_level: community
id: argument-injection-ssh-keygen
namespace: argument:injection:ssh-keygen
name: ssh-keygen
description: "Argument injection via ssh-keygen"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "ssh-keygen"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Loads a local library. See (https://seanpesce.blogspot.com/2023/03/leveraging-ssh-keygen-for-arbitrary.html)[this blog) for more information."
    command: "ssh-keygen -D lib.so
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/ssh-keygen/"
---

# ssh-keygen

GTFOArgs entry for ssh-keygen. This binary can be used to inject arguments for execution, file operations, or other capabilities.
