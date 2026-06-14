---
trust_level: community
id: argument-injection-unzip
namespace: argument:injection:unzip
name: unzip
description: Argument injection via unzip
version: 1.0.0
capabilities:
- system.file.write
- system.file.read
platforms:
- cross-platform
techniques:
- exfiltration
- discovery
execution:
  template: unzip
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Can be used to change the location the file is unzipped. In this example,
    the files are unzipped to /root/.
  command: 'unzip -d /root/ archive.zip -d /tmp/ '
- description: Can be used to read locate archives. The contents of the files and
    the filenames are shown.
  command: 'unzip -c archive.zip '
- description: Can be used to read locate archives. The contents of the files are
    shown.
  command: 'unzip -p archive.zip '
references:
- label: GTFOArgs
  url: https://gtfoargs.github.io/gtfoargs/unzip/
features:
- compression
- file-system
- local
- stealth
---

# unzip

GTFOArgs entry for unzip. This binary can be used to inject arguments for execution, file operations, or other capabilities.
