---
trust_level: community
id: wtfbin-veritas-backup-agent
namespace: wtf:bin:veritas-backup-agent
name: Veritas Backup Agent (Symantec)
description: Another bin with an identity crisis
version: 1.0.0
capabilities:
- credential.discovery.whoami
platforms:
- windows
techniques:
- discovery
execution:
  template: Veritas Backup Agent
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
- label: Documentation
  url: https://github.com/mttaggart/wtfbins/issues/62
- label: WTFBins
  url: https://wtfbins.netlify.app/wtfbins/veritas-backup-agent/
features:
- file-system
---

examples:
  - description: "Execute Veritas Backup Agent (Symantec) and observe the unusual behavior"
    command: "Veritas Backup Agent"

# Veritas Backup Agent (Symantec)

Another bin with an identity crisis.



[Microsoft Management Services Cloud Managed Desktop Agent](https://learn.microsoft.com/en-us/managed-desktop/overview/service-plan) runs b64 PowerShell.

*Contributed by Alexandros Pappas (redblueops)*
