---
trust_level: community
id: argument-injection-chrome
namespace: argument:injection:chrome
name: chrome
description: "Argument injection via chrome"
version: "1.0.0"
capabilities:
  - security.execution.command
platforms:
  - cross-platform
techniques:
  - execution
execution:
  template: "chrome"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "The `--gpu-launcher` flag executes a command. This is particularly relevant for Electron applications."
    command: "chrome '--gpu-launcher=\"id>/tmp/foo\"'
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/chrome/"
---

# chrome

GTFOArgs entry for chrome. This binary can be used to inject arguments for execution, file operations, or other capabilities.
