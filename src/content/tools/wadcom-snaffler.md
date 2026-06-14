---
trust_level: community
id: wadcom-snaffler
namespace: wadcom:tool:snaffler
name: Snaffler
description: Snaffler is a tool used to enumerate sensitive data (passwords, PII,
  etc.) from file shares in Active Directory. It searches for interesting files based
  on file extensions, file names, and file content that's matched against regex. It's
  also highly configurable, allowing you to add your own regex searches. The following
  command will enumerate all machines in the domain and search for accessible file
  shares, checking for interesting files that might have sensitive data.
version: 1.0.0
capabilities:
- network.enumerate.shares
platforms:
- windows
techniques:
- discovery
execution:
  template: snaffler
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Command execution
  command: Snaffler.exe -s -o snaffler_output.log -d test.local -c 10.10.10.1
references:
- label: Reference 1
  url: https://github.com/SnaffCon/Snaffler
items:
- Password
- Hash
services:
- SMB
features:
- file-system
- local
- network-intensive
- pipes-stdin
---

# Snaffler

Snaffler is a tool used to enumerate sensitive data (passwords, PII, etc.) from file shares in Active Directory. It searches for interesting files based on file extensions, file names, and file content that's matched against regex. It's also highly configurable, allowing you to add your own regex searches. The following command will enumerate all machines in the domain and search for accessible file shares, checking for interesting files that might have sensitive data.

Command Reference:

	Domain: test.local

	Domain Controller: 10.10.10.1

```
Snaffler.exe -s -o snaffler_output.log -d test.local -c 10.10.10.1
```

**Services:** SMB

**Required:** Shell
