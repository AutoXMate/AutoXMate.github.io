---
trust_level: community
id: darkiros-chisel
namespace: darkiros:tool:chisel
name: chisel
description: chisel server (server on local machine)
version: 1.0.0
capabilities:
- network.pivot.generic
platforms:
- cross-platform
techniques:
- lateral-movement
execution:
  template: chisel
  sandbox: execFile
  timeout_seconds: 30
  shell: false
examples:
- description: chisel server (server on local machine)
  command: chisel server -p [port] --reverse
- description: chisel reverse port forwarding (client on remote machine) - forward
    client port on server
  command: chisel client -v [server_ip]:[server_port] R:[serverside_port]:[clientside_host|localhost]:[clientside_port]
- description: chisel remote port forwarding (client on remote machine) - forward
    server port on client
  command: chisel client -v [server_ip]:[server_port|8000] [clientside_host|0.0.0.0]:[clientside_port]:[serverside_host|127.0.0.1]:[serverside_port]
- description: chisel socks proxy (client on remote machine)
  command: chisel client [server_ip]:[server_port] R:socks
references:
- label: Source
  url: https://github.com/jpillora/chisel
- label: Darkiros
  url: https://darkiros.github.io/commands.html
items:
- NoCreds
services:
- HTTP
- HTTPS
- RPC
- SMB
features:
- local
- network-intensive
- remote
---

# chisel

Darkiros cheat sheet commands:

**chisel server (server on local machine)**
```
chisel server -p [port] --reverse
```

**chisel reverse port forwarding (client on remote machine) - forward client port on server**
```
chisel client -v [server_ip]:[server_port] R:[serverside_port]:[clientside_host|localhost]:[clientside_port]
```

**chisel remote port forwarding (client on remote machine) - forward server port on client**
```
chisel client -v [server_ip]:[server_port|8000] [clientside_host|0.0.0.0]:[clientside_port]:[serverside_host|127.0.0.1]:[serverside_port]
```

**chisel socks proxy (client on remote machine)**
```
chisel client [server_ip]:[server_port] R:socks
```
