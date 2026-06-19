---
id: security-recon-nmap
namespace: security:recon:nmap
name: nmap
description: Network discovery and security auditing scanner used for host discovery,
  port scanning, and service detection.
author: Repository Maintainers
version: 1.0.0
capabilities:
- network.discovery.host
- network.scan.port
- network.scan.service
- security.fingerprint.os
- security.fingerprint.service
- security.audit.script
- security.evasion.firewall
platforms:
- linux
- macos
- windows
- cross-platform
risk_level: medium
trust_level: verified
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools:
- masscan
- rustscan
- zenmap
artifacts:
- type: network.scan.nmap.xml
  description: Structured Nmap XML output with port and service details
  mime: application/xml
  schema_version: 1.0.0
  trust_level: verified
- type: network.scan.nmap.json
  description: JSON-formatted scan results
  mime: application/json
  schema_version: 1.0.0
  trust_level: verified
- type: network.scan.nmap.grepable
  description: Legacy grepable format for text processing
  mime: text/plain
  trust_level: community
workflow_edges:
  produces:
  - scan-results
  - host-list
  - open-ports
  consumes:
  - target-ip
  - target-range
contract:
  inputs:
  - type: network.target.ip
    description: Target IP address or hostname
  - type: network.target.range
    description: IP range or CIDR notation
  outputs:
  - type: network.scan.nmap.xml
    description: Structured scan results in XML format
    mime: application/xml
    schema_version: 1.0.0
  - type: network.scan.nmap.json
    description: Scan results as JSON
    mime: application/json
    schema_version: 1.0.0
  side_effects:
  - network_traffic
  - raw_socket_access
  resource_cost:
    cpu: medium
    memory_mb: 256
    network: high
    disk_io: low
resource_profile:
  cpu: medium
  memory_mb: 256
  network: high
  disk_io: low
allowed-tools:
- nmap
- Bash
- execFile
parameters:
- name: flag-i
  type: string
  required: false
  description: Set the flag-i parameter
  aliases:
  - -i
- name: flag-i-2
  type: string
  required: false
  description: Set the flag-i-2 parameter
  aliases:
  - -i
- name: exclude
  type: string
  required: false
  description: Set the exclude parameter
  aliases:
  - --exclude <host1[,host2][,host3],...>
- name: excludefile
  type: file
  required: false
  description: Set the excludefile parameter
  aliases:
  - --excludefile <exclude_file>
- name: flag-s
  type: string
  required: false
  description: List Scan - simply list targets to scan
  aliases:
  - -s
- name: flag-s-2
  type: string
  required: false
  description: Ping Scan - disable port scan
  aliases:
  - -s
- name: flag-P
  template_key: flag-p
  type: string
  required: false
  description: Treat all hosts as online -- skip host discovery
  aliases:
  - -P
- name: flag-P-2
  template_key: flag-p-2
  type: string
  required: false
  description: TCP SYN, TCP ACK, UDP or SCTP discovery to given ports
  aliases:
  - -P
- name: flag-P-3
  template_key: flag-p-3
  type: string
  required: false
  description: ICMP echo, timestamp, and netmask request discovery probes
  aliases:
  - -P
- name: flag-P-4
  template_key: flag-p-4
  type: string
  required: false
  description: Set the flag-P-4 parameter
  aliases:
  - -P
- name: flag-n
  type: string
  required: false
  default_value: sometimes
  description: Never do DNS resolution/Always resolve
  aliases:
  - -n
  - -R
- name: dns-servers
  type: string
  required: false
  description: Set the dns-servers parameter
  aliases:
  - --dns-servers <serv1[,serv2],...>
- name: system-dns
  type: string
  required: false
  description: Set the system-dns parameter
  aliases:
  - --system-dns
- name: traceroute
  type: string
  required: false
  description: Set the traceroute parameter
  aliases:
  - --traceroute
- name: flag-s-3
  type: string
  required: false
  description: TCP SYN/Connect()/ACK/Window/Maimon scans
  aliases:
  - -s
- name: flag-s-4
  type: string
  required: false
  description: UDP Scan
  aliases:
  - -s
- name: flag-s-5
  type: string
  required: false
  description: TCP Null, FIN, and Xmas scans
  aliases:
  - -s
- name: scanflags
  type: string
  required: false
  description: Set the scanflags parameter
  aliases:
  - --scanflags <flags>
- name: flag-s-6
  type: string
  required: false
  description: Set the flag-s-6 parameter
  aliases:
  - -s
- name: flag-s-7
  type: string
  required: false
  description: SCTP INIT/COOKIE-ECHO scans
  aliases:
  - -s
- name: flag-s-8
  type: string
  required: false
  description: IP protocol scan
  aliases:
  - -s
- name: flag-b
  type: string
  required: false
  description: Set the flag-b parameter
  aliases:
  - -b
- name: flag-p
  type: string
  required: false
  description: Set the flag-p parameter
  aliases:
  - -p
- name: exclude-ports
  type: string
  required: false
  description: Set the exclude-ports parameter
  aliases:
  - --exclude-ports <port ranges>
- name: flag-r
  type: string
  required: false
  description: Scan ports sequentially - don't randomize
  aliases:
  - -r
- name: top-ports
  type: integer
  required: false
  description: Set the top-ports parameter
  aliases:
  - --top-ports <number>
- name: port-ratio
  type: string
  required: false
  description: Set the port-ratio parameter
  aliases:
  - --port-ratio <ratio>
- name: flag-s-9
  type: string
  required: false
  description: Probe open ports to determine service/version info
  aliases:
  - -s
- name: version-intensity
  type: integer
  required: false
  description: Set the version-intensity parameter
  aliases:
  - --version-intensity <level>
- name: version-light
  type: string
  required: false
  description: Set the version-light parameter
  aliases:
  - --version-light

- name: PE
  type: boolean
  required: false
  description: "/PP/PM: ICMP echo, timestamp, and netmask request discovery probes"
  aliases:
    - "-PE"
- name: PO
  type: boolean
  required: false
  description: "IP Protocol Ping"
  aliases:
    - "-PO"
- name: PS
  type: boolean
  required: false
  description: "/PA/PU/PY[portlist]: TCP SYN, TCP ACK, UDP or SCTP discovery to given ports"
  aliases:
    - "-PS"
- name: Pn
  type: boolean
  required: false
  description: "Treat all hosts as online -- skip host discovery"
  aliases:
    - "-Pn"
- name: append-output
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--append-output"
- name: badsum
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--badsum"
- name: data
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--data <hex string>"
- name: data-length
  type: integer
  required: false
  default: null
  description: ""
  aliases:
    - "--data-length <num>"
- name: data-string
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--data-string <string>"
- name: datadir
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--datadir <dirname>"
- name: flag-6
  type: string
  required: false
  default: null
  description: "Enable IPv6 scanning"
  aliases:
    - "-6"
- name: flag-D
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-D"
- name: flag-S
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-S"
- name: flag-T
  type: string
  required: false
  default: null
  description: "Set timing template (higher is faster)"
  aliases:
    - "-T"
    - "-5"
- name: flag-d
  type: string
  required: false
  default: null
  description: "Increase debugging level (use -dd or more for greater effect)"
  aliases:
    - "-d"
- name: flag-e
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-e"
- name: flag-h
  type: string
  required: false
  default: null
  description: "Print this help summary page"
  aliases:
    - "-h"
- name: flag-o
  type: file
  required: false
  default: null
  description: "and Grepable format, respectively, to the given filename"
  aliases:
    - "-o"
    - "-o"
    - "-o"
    - "-o"
- name: flag-o-2
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-o"
- name: flag-s-10
  type: string
  required: false
  default: null
  description: "equivalent to --script=default"
  aliases:
    - "-s"
- name: flag-v
  type: string
  required: false
  default: null
  description: "Increase verbosity level (use -vv or more for greater effect)"
  aliases:
    - "-v"
- name: host-timeout
  type: number
  required: false
  default: null
  description: ""
  aliases:
    - "--host-timeout <time>"
- name: iL
  type: boolean
  required: false
  description: "Input from list of hosts/networks"
  aliases:
    - "-iL"
- name: iR
  type: boolean
  required: false
  description: "Choose random targets"
  aliases:
    - "-iR"
- name: iflist
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--iflist"
- name: ip-options
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--ip-options <options>"
- name: max-rate
  type: integer
  required: false
  default: null
  description: ""
  aliases:
    - "--max-rate <number>"
- name: max-retries
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--max-retries <tries>"
- name: min-hostgroup
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-h"
    - "--min-hostgroup"
- name: min-parallelism
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-p"
    - "--min-parallelism"
- name: min-rate
  type: integer
  required: false
  default: null
  description: ""
  aliases:
    - "--min-rate <number>"
- name: min-rtt-timeout
  type: string
  required: false
  default: null
  description: "probe round trip time"
  aliases:
    - "-r"
    - "-t"
    - "-r"
    - "-t"
    - "--min-rtt-timeout"
- name: mtu
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-f"
    - "--mtu <val>"
- name: no-stylesheet
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--no-stylesheet"
- name: noninteractive
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--noninteractive"
- name: oA
  type: boolean
  required: false
  description: "Output in the three major formats at once"
  aliases:
    - "-oA"
- name: oX
  type: boolean
  required: false
  description: "Output scan in normal, XML, s|<rIpt kIddi3,"
  aliases:
    - "-oX"
    - "-oS"
    - "-oG"
- name: open
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--open"
- name: osscan-guess
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--osscan-guess"
- name: osscan-limit
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--osscan-limit"
- name: packet-trace
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--packet-trace"
- name: privileged
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--privileged"
- name: proxies
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--proxies <url1,[url2],...>"
- name: reason
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--reason"
- name: resume
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--resume <filename>"
- name: sC
  type: boolean
  required: false
  description: "equivalent to --script=default"
  aliases:
    - "-sC"
- name: sI
  type: boolean
  required: false
  description: "Idle scan"
  aliases:
    - "-sI"
- name: sL
  type: boolean
  required: false
  description: "List Scan - simply list targets to scan"
  aliases:
    - "-sL"
- name: sN
  type: boolean
  required: false
  description: "/sF/sX: TCP Null, FIN, and Xmas scans"
  aliases:
    - "-sN"
- name: sO
  type: boolean
  required: false
  description: "IP protocol scan"
  aliases:
    - "-sO"
- name: sS
  type: boolean
  required: false
  description: "/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans"
  aliases:
    - "-sS"
- name: sU
  type: boolean
  required: false
  description: "UDP Scan"
  aliases:
    - "-sU"
- name: sV
  type: boolean
  required: false
  description: "Probe open ports to determine service/version info"
  aliases:
    - "-sV"
- name: sY
  type: boolean
  required: false
  description: "/sZ: SCTP INIT/COOKIE-ECHO scans"
  aliases:
    - "-sY"
- name: scan-delay
  type: number
  required: false
  default: null
  description: ""
  aliases:
    - "--scan-delay"
    - "--max-scan-delay <time>"
- name: script
  type: string
  required: false
  default: null
  description: "directories, script-files or script-categories"
  aliases:
    - "--script"
- name: script-args
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--script-args"
- name: script-args-file
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--script-args-file"
- name: script-help
  type: array
  required: false
  default: null
  description: "<Lua scripts> is a comma-separated list of script-files or script-categories"
  aliases:
    - "--script-help"
- name: script-trace
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--script-trace"
- name: script-updatedb
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--script-updatedb"
- name: send-eth
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--send-eth"
    - "--send-ip"
- name: sn
  type: boolean
  required: false
  description: "Ping Scan - disable port scan"
  aliases:
    - "-sn"
- name: source-port
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-g"
    - "--source-port <portnum>"
- name: spoof-mac
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--spoof-mac <mac address/prefix/vendor name>"
- name: stylesheet
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--stylesheet <path/URL>"
- name: ttl
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "-t"
    - "-l"
    - "--ttl <val>"
- name: unprivileged
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--unprivileged"
- name: version-all
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--version-all"
- name: version-trace
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--version-trace"
- name: webxml
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--webxml"

execution:
  template: nmap {flag-i} {flag-i-2} {exclude} {excludefile} {flag-s}
  sandbox: execFile
  timeout_seconds: 300
  shell: false
  container:
    image: instrumentisto/nmap
global_vars:
  target: ip
examples:
- description: Basic port scan of a target
  command: nmap -sS -T4 scanme.nmap.org
- description: Full service and OS detection
  command: nmap -sS -sV -O -T4 scanme.nmap.org
- description: Scan specific ports with default NSE scripts
  command: nmap -sS -sC -p 22,80,443 scanme.nmap.org
- description: UDP scan of top 100 ports
  command: nmap -sU --top-ports 100 scanme.nmap.org
- description: Nmap's `krb5-enum-users` script attempts to bruteforce and enumerate
    valid Active Directory accounts through Kerberos Pre-Authentication
  command: nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='test.local',userdb=usernames.txt
    10.10.10.1
- description: 'Darkiros RECON: Nmap - hosts alive'
  command: nmap -sn [ip_range]
- description: 'Darkiros RECON: Nmap - classic scan'
  command: nmap -sC -sV [ip]
- description: 'Darkiros RECON: Nmap - read targets from file'
  command: nmap -iL [file]
- description: 'Darkiros RECON: Nmap - scan all port full'
  command: nmap -Pn -sC -sV -p [port] [ip] -oN scan.txt --reason --script=vuln
- description: 'Darkiros RECON: Nmap - UDP scan'
  command: nmap -sU [ip]
- description: 'Darkiros RECON: Nmap - SMB signin disabled'
  command: nmap -Pn -sS -T4 --open --script smb-security-mode -p 445 [ip]
- description: 'Darkiros RECON: Nmap - kerberos user enumeration'
  command: nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm=[domain]
    [dc-ip]
- description: 'Darkiros RECON: Nmap - showmount'
  command: nmap -sV --script=nfs-showmount [ip]
- description: 'Darkiros RECON: VNC - nmap enum'
  command: nmap -sV -p [port|5900] --script=realvnc-auth-bypass,vnc-info,vnc-title
    [ip]
- description: 'Darkiros RECON: mssql - enum'
  command: nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes
    --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER
    -sV -p [port|1433] [IP]
- description: 'Darkiros RECON: nmap - pop3 infos'
  command: nmap --script "pop3-capabilities or pop3-ntlm-info" -sV -port [port] [ip]
- description: 'Darkiros RECON: nmap - mysql enumeration'
  command: nmap -sV -p 3306 --script mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122
    [ip]
- description: 'Darkiros ATTACK/CONNECT: nmap - FTP enum anonym'
  command: nmap --script ftp-anon -p 21 [ip]
- description: 'Darkiros ATTACK/CONNECT: nmap - x11 check anonymous connection'
  command: nmap --script x11-access -p 6000-6063 -sV [ip]
- description: 'Darkiros RECON: nmap - snmp scan'
  command: nmap -sU -p 161 -sC --open [ip]
- description: 'Darkiros ATTACK/BRUTEFORCE: nmap - snmp brute force'
  command: nmap -sU -p 161 --script snmp-brute --script-args snmpbrute.communitiesdb=[wordlist]
    [ip]
- description: NetRunners Active Directory/enumeration
  command: nmap -p- --open -sS --min-rate 5000 -n -Pn {{IP}} -vvv
- description: NetRunners KERBEROS/enumeration
  command: nmap -p- --open -sS --min-rate 5000 -n -Pn {{IP}} -vvv
- description: NetRunners web/enumeration
  command: nmap -p- --open -sS --min-rate 5000 -n -Pn {{IP}} -vvv
- description: 'Single target scan:'
  command: nmap [target]
- description: 'Scan from a list of targets:'
  command: nmap -iL [list.txt]
- description: Scan port for all available A records (useful when multiple A records
    are returned by the DNS server)
  command: nmap --script resolveall \
- description: 'cheat.sheets: nmap'
  command: --script-args newtargets,resolveall.hosts=[target] -p [port]
- description: 'iPv6:'
  command: nmap -6 [target]
- description: 'OS detection:'
  command: nmap -O --osscan_guess [target]
- description: 'Save output to text file:'
  command: nmap -oN [output.txt] [target]
- description: 'Save output to xml file:'
  command: nmap -oX [output.xml] [target]
- description: 'Scan a specific port:'
  command: nmap -p [port] [target]
- description: 'Do an aggressive scan:'
  command: nmap -A [target]
- description: 'Speedup your scan: -n => disable ReverseDNS --min-rate=X => min X
    packets / sec'
  command: nmap -T5 --min-parallelism=50 -n --min-rate=300 [target]
- description: 'Traceroute:'
  command: nmap -traceroute [target]
- description: 'Example: Ping scan all machines on a class C network'
  command: nmap -sP 192.168.0.0/24
- description: 'Use some script:'
  command: nmap --script default,safe
- description: Loads the script in the default category, the banner script, and all
    .nse files in the directory /home/user/customscripts.
  command: nmap --script default,banner,/home/user/customscripts
- description: Loads all scripts whose name starts with http-, such as http-auth and
    http-open-proxy.
  command: nmap --script 'http-*'
- description: Loads every script except for those in the intrusive category.
  command: nmap --script "not intrusive"
- description: Loads those scripts that are in both the default and safe categories.
  command: nmap --script "default and safe"
- description: Loads scripts in the default, safe, or intrusive categories, except
    for those whose names start with http-.
  command: nmap --script "(default or safe or intrusive) and not http-*"
- description: Scan for the heartbleed -pT:443 => Scan only port 443 with TCP (T:)
  command: nmap -T5 --min-parallelism=50 -n --script "ssl-heartbleed" -pT:443 127.0.0.1
- description: Show all information (debug mode)
  command: nmap -d ...
- description: Discover DHCP information on an interface
  command: nmap --script broadcast-dhcp-discover -e eth0
references:
- label: Nmap official documentation
  url: https://nmap.org/docs.html
- label: Nmap Network Scanning book
  url: https://nmap.org/book/
- label: NSE script reference
  url: https://nmap.org/nsedoc/
phase: enumeration
techniques:
- command-and-control
- discovery
- enumeration
- lateral-movement
items:
- NoCreds
services:
- Kerberos
attack_types:
- Enumeration
install:
- method: apt
  package_name: nmap
  commands:
  - apt-get install -y nmap
- method: brew
  package_name: nmap
  commands:
  - brew install nmap
features:
- network-intensive
- pipes-stdin
- pipes-stdout
- process-manip
mitre_ids:
- T1046
- T1595
---

# Nmap — Network Mapper

Nmap (Network Mapper) is the industry-standard open-source utility for network discovery, security auditing, and vulnerability assessment. It uses raw IP packets to determine which hosts are available on a network, what services those hosts are offering, what operating systems they are running, and what packet filters/firewalls are in use.

## Scan Types

| Scan Flag | Type              | Description                          | Requires Privilege |
|-----------|-------------------|--------------------------------------|--------------------|
| `-sS`     | SYN scan          | Half-open TCP scan (stealth)         | Yes                |
| `-sT`     | TCP connect scan  | Full TCP connection scan             | No                 |
| `-sU`     | UDP scan          | UDP service discovery                | Yes                |
| `-sA`     | ACK scan          | Firewall rule mapping                | Yes                |
| `-sV`     | Version detection | Service version fingerprinting       | Varies             |
| `-sC`     | Default scripts   | Common NSE script execution          | Varies             |

## Nmap Scripting Engine (NSE)

NSE extends nmap with over 600 scripts for:

- **Vulnerability detection**: `vuln` category scripts
- **Service enumeration**: `discovery`, `safe` categories
- **Authentication testing**: `auth` category
- **Brute force attacks**: `brute` category
- **Exploitation**: `exploit` category

```bash
# Run all vulnerability scripts
nmap --script vuln target

# Run all safe scripts for service enumeration
nmap -sV --script "safe or discovery" target
```

## Output Formats

```bash
# Normal output (default)
nmap target

# XML output (machine-parseable)
nmap -oX scan.xml target

# Grepable output (legacy)
nmap -oG scan.gnmap target

# JSON output (modern structured)
nmap -oJ scan.json target

# All formats simultaneously
nmap -oA scan target
```

## Operational Security

- SYN scans (`-sS`) require root privileges on Linux/MacOS
- Aggressive timing (`-T5`) can cause denial-of-service; use responsibly
- Scan without authorization is illegal in many jurisdictions
- Use decoy scans (`-D`) or idle scans (`-sI`) for operational stealth

## Related Tools

- **[masscan](../../recon/masscan.md)** — High-speed port scanner for large address spaces
- **[RustScan](../../recon/rustscan.md)** — Fast port scanner with Nmap integration
- **[netcat](../../socket/nc.md)** — Raw socket interaction for manual service probing
