---
id: network-capture-tcpdump
namespace: network:capture:tcpdump
name: tcpdump
description: Dump traffic on a network interface
author: "Repository Maintainers"
version: "1.0.0"
capabilities:
  - network.capture.tcpdump
  - network.capture.packet
  - network.capture.sniff
platforms:
  - linux
risk_level: low
trust_level: verified
execution_policy: enabled
architectures:
  - amd64
  - arm64
features:
  - remote
  - network-intensive
  - requires-root
  - streaming
techniques:
  - network-sniffing
  - discovery
  - recon
  - command-and-control
parameters:
  - name: flag-r
    type: array
    required: false
    description: "read packets from a network interface. It can also be run with the
      -V flag, which causes it to read a list of saved packet files. In all cases,
      only packets that match expression will be processed ..."
    aliases:
      - -r
  - name: flag-b
    type: string
    required: false
    description: "Print the AS number in BGP packets in ASDOT notation rather than"
    aliases:
      - -b
  - name: flag-B
    template_key: flag-b
    type: string
    required: false
    description: "--buffer-size=buffer_size Set the operating system capture buffer
      size to buffer_size, in units of KiB (1024 bytes)"
    aliases:
      - -B
  - name: flag-c
    type: string
    required: false
    description: "Exit after receiving count packets"
    aliases:
      - -c
  - name: count
    type: string
    required: false
    description: "Print only on stdout the packet count when reading capture file(s)
      instead of parsing/printing the packets. If a filter is specified on the command
      line, tcpdump counts only packets that were match..."
    aliases:
      - --count
  - name: flag-C
    template_key: flag-c
    type: string
    required: false
    description: "Before writing a raw packet to a savefile, check whether the file
      is currently larger than file_size and, if so, close the current savefile and
      open a new one. Savefiles after the first savefile wi..."
    aliases:
      - -C
  - name: flag-d
    type: string
    required: false
    description: "Dump the compiled packet-matching code in a human readable form"
    aliases:
      - -d
  - name: flag-i
    type: string
    required: false
    description: "In this case the DLT defaults to EN10MB and can be set to"
    aliases:
      - -i
  - name: flag-d-2
    type: string
    required: false
    description: "Dump packet-matching code as a C program fragment"
    aliases:
      - -d
  - name: flag-d-3
    type: string
    required: false
    description: "Dump packet-matching code as decimal numbers (preceded with a"
    aliases:
      - -d
  - name: flag-D
    template_key: flag-d
    type: array
    required: false
    description: "--list-interfaces Print the list of the network interfaces available
      on the system and on which tcpdump can capture packets. For each network in‐
      terface, a number and an interface name, possibly f..."
    aliases:
      - -D
  - name: flag-a
    type: string
    required: false
    description: "where the interface name is a somewhat complex string"
    aliases:
      - -a
  - name: flag-e
    type: string
    required: false
    description: "Print the link-level header on each dump line. This can be used"
    aliases:
      - -e
  - name: flag-f
    type: integer
    required: false
    description: "Print `foreign' IPv4 addresses numerically rather than symboli‐"
    aliases:
      - -f
  - name: flag-F
    template_key: flag-f
    type: string
    required: false
    description: "Use file as input for the filter expression. An additional ex‐ pression
      given on the command line is ignored"
    aliases:
      - -F
  - name: flag-g
    type: string
    required: false
    description: "--ip-oneline Do not insert a line break after the IP header in verbose
      mode"
    aliases:
      - -g
  - name: flag-G
    template_key: flag-g
    type: file
    required: false
    description: "If specified, rotates the dump file specified with the -w option
      every rotate_seconds seconds. Savefiles will have the name spec‐ ified by -w
      which should include a time format as defined by strfti..."
    aliases:
      - -G
  - name: flag-h
    type: string
    required: false
    description: "--help Print the tcpdump and libpcap version strings, print a usage
      mes‐ sage, and exit"
    aliases:
      - -h
  - name: version
    type: string
    required: false
    description: "Print the tcpdump and libpcap version strings and exit"
    aliases:
      - --version
  - name: flag-i-2
    type: array
    required: false
    description: "--interface=interface Listen, report the list of link-layer types,
      report the list of time stamp types, or report the results of compiling a filter
      ex‐ pression on interface. If unspecified and if ..."
    aliases:
      - -i
  - name: flag-I
    template_key: flag-i
    type: string
    required: false
    description: "--monitor-mode Put the interface in \"monitor mode\"; this is supported
      only on IEEE 802.11 Wi-Fi interfaces, and supported only on some operat‐ ing
      systems"
    aliases:
      - -I
  - name: immediate-mode
    type: string
    required: false
    description: "Capture in \"immediate mode\". In this mode, packets are delivered
      to tcpdump as soon as they arrive, rather than being buffered for efficiency.
      This is the default when printing packets rather tha..."
    aliases:
      - --immediate-mode
  - name: flag-j
    type: string
    required: false
    description: "--time-stamp-type=tstamp_type Set the time stamp type for the capture
      to tstamp_type. The names to use for the time stamp types are given in pcap-tstamp(7);
      not all the types listed there will nece..."
    aliases:
      - -j
  - name: flag-J
    template_key: flag-j
    type: string
    required: false
    description: "--list-time-stamp-types List the supported time stamp types for
      the interface and exit. If the time stamp type cannot be set for the interface,
      no time stamp types are listed"
    aliases:
      - -J
  - name: time-stamp-precision
    type: number
    required: false
    description: "When capturing, set the time stamp precision for the capture to
      tstamp_precision. Note that availability of high precision time stamps (nanoseconds)
      and their actual accuracy is platform and hardwa..."
    aliases:
      - --time-stamp-precision
  - name: micro
    type: number
    required: false
    description: "--nano Shorthands for --time-stamp-precision=micro or --time-stamp-pre‐
      cision=nano, adjusting the time stamp precision accordingly. When reading packets
      from a savefile, using --micro truncates ti..."
    aliases:
      - --micro
  - name: flag-K
    template_key: flag-k
    type: string
    required: false
    description: "--dont-verify-checksums Don't attempt to verify IP, TCP, or UDP
      checksums. This is use‐ ful for interfaces that perform some or all of those
      checksum calculation in hardware; otherwise, all outgoin..."
    aliases:
      - -K
  - name: flag-l
    type: string
    required: false
    description: "Make stdout line buffered. Useful if you want to see the data"
    aliases:
      - -l
  - name: flag-U
    template_key: flag-u
    type: string
    required: false
    description: "be ``packet-buffered'', so that the output is written to stdout
      at the end of each packet rather than at the end of each line; this is buffered
      on all platforms, including Windows"
    aliases:
      - -U
      - -l
  - name: flag-L
    template_key: flag-l
    type: array
    required: false
    description: "--list-data-link-types List the known data link types for the interface,
      in the speci‐ fied mode, and exit. The list of known data link types may be
      dependent on the specified mode; for example, on..."
    aliases:
      - -L

  - name: XX
    type: boolean
    required: false
    description: "When parsing and printing, in addition to printing the headers of"
    aliases:
      - "-XX"
  - name: absolute_tcp_sequence_numbers
    type: boolean
    required: false
    description: ""
    aliases:
      - "--absolute-tcp-sequence-numbers"
  - name: buffer_size
    type: boolean
    required: false
    description: ""
    aliases:
      - "--buffer-size"
  - name: dd
    type: boolean
    required: false
    description: "code as a C program fragment."
    aliases:
      - "-dd"
      - "-matching"
  - name: ddd
    type: boolean
    required: false
    description: "code as decimal  numbers  (preceded  with  a"
    aliases:
      - "-ddd"
      - "-matching"
  - name: direction
    type: boolean
    required: false
    description: ""
    aliases:
      - "--direction"
  - name: dont_verify_checksums
    type: boolean
    required: false
    description: ""
    aliases:
      - "--dont-verify-checksums"
  - name: flag-M
    type: string
    required: false
    default: null
    description: "Use secret as a shared secret for validating the digests found in TCP segments with the TCP-MD5 option (RFC 2385), if present"
    aliases:
      - "-M"
  - name: flag-O
    type: string
    required: false
    default: null
    description: "--no-optimize Do not run the packet-matching code optimizer. This is useful only if you suspect a bug in the optimizer"
    aliases:
      - "-O"
  - name: flag-Q
    type: string
    required: false
    default: null
    description: "--direction=direction Choose send/receive direction direction for which packets should be captured. Possible values are `in', `out' and `inout'. Not available on all platforms"
    aliases:
      - "-Q"
  - name: flag-S
    type: string
    required: false
    default: null
    description: "--absolute-tcp-sequence-numbers Print absolute, rather than relative, TCP sequence numbers"
    aliases:
      - "-S"
  - name: flag-T
    type: string
    required: false
    default: null
    description: "Force packets selected by \"expression\" to be interpreted the specified type. Currently known types are aodv (Ad-hoc On-demand Distance Vector protocol), carp (Common Address Redundancy Proto‐ col), cnfp (Cisco NetFlow protocol), domain (Domain Name System), lmp (Link Management Protocol), pgm (Pragmatic General Multi‐ cast), pgm_zmtp1 (ZMTP/1.0 inside PGM/EPGM), ptp (Precision Time Protocol), radius (RADIUS), resp (REdis Serialization Protocol), rpc (Remote Procedure Call), rtcp (Real-Time Applications control protocol), rtp (Real-Time Applications protocol), snmp (Simple Network Management Protocol), someip (SOME/IP), tftp (Trivial File Transfer Protocol), vat (Visual Audio Tool), vxlan (Virtual eXtensible Local Area Network), wb (distributed White Board) and zmtp1 (ZeroMQ Message Transport Protocol 1.0)"
    aliases:
      - "-T"
  - name: flag-U-2
    type: string
    required: false
    default: null
    description: "--packet-buffered If the -w option is not specified, or if it is specified but the --print flag is also specified, make the printed packet output ``packet-buffered''; i.e., as the description of the contents of each packet is printed, it will be written to the standard out‐ put, rather than, when not writing to a terminal, being written only when the output buffer fills"
    aliases:
      - "-U"
  - name: flag-V
    type: file
    required: false
    default: null
    description: "Read a list of filenames from file. Standard input is used if file is ``-''"
    aliases:
      - "-V"
  - name: flag-W
    type: integer
    required: false
    default: null
    description: "Used in conjunction with the -C option, this will limit the num‐ ber of files created to the specified number, and begin overwrit‐ ing files from the beginning, thus creating a 'rotating' buffer. In addition, it will name the files with enough leading 0s to support the maximum number of files, allowing them to sort cor‐ rectly"
    aliases:
      - "-W"
  - name: flag-Z
    type: string
    required: false
    default: null
    description: "--relinquish-privileges=user If tcpdump is running as root, after opening the capture device or input savefile, but before opening any savefiles for output, change the user ID to user and the group ID to the primary group of user"
    aliases:
      - "-Z"
  - name: flag-m
    type: string
    required: false
    default: null
    description: "Load SMI MIB module definitions from file module. This option can be used several times to load several MIB modules into tcp‐ dump"
    aliases:
      - "-m"
  - name: flag-n
    type: integer
    required: false
    default: null
    description: "Don't convert addresses (i.e., host addresses, port numbers"
    aliases:
      - "-n"
  - name: flag-p
    type: string
    required: false
    default: null
    description: "--no-promiscuous-mode Don't put the interface into promiscuous mode. Note that the in‐ terface might be in promiscuous mode for some other reason; hence, `-p' cannot be used as an abbreviation for `ether host {local-hw-addr} or ether broadcast'"
    aliases:
      - "-p"
  - name: flag-q
    type: string
    required: false
    default: null
    description: "Quick (quiet?) output. Print less protocol information so output"
    aliases:
      - "-q"
  - name: flag-r-2
    type: string
    required: false
    default: null
    description: "Read packets from file (which was created with the -w option or by other tools that write pcap or pcapng files). Standard input is used if file is ``-''"
    aliases:
      - "-r"
  - name: flag-s
    type: string
    required: false
    default: null
    description: "--snapshot-length=snaplen Snarf snaplen bytes of data from each packet rather than the de‐ fault of 262144 bytes. Packets truncated because of a limited snapshot are indicated in the output with ``[|proto]'', where proto is the name of the protocol level at which the truncation has occurred"
    aliases:
      - "-s"
  - name: flag-t
    type: string
    required: false
    default: null
    description: "Don't print a timestamp on each dump line"
    aliases:
      - "-t"
  - name: flag-t-2
    type: number
    required: false
    default: null
    description: "Print the timestamp, as seconds since January 1, 1970, 00:00:00"
    aliases:
      - "-t"
  - name: flag-t-3
    type: number
    required: false
    default: null
    description: "Print a delta (microsecond or nanosecond resolution depending on"
    aliases:
      - "-t"
  - name: flag-t-4
    type: number
    required: false
    default: null
    description: "second since midnight, preceded by the date, on each dump line"
    aliases:
      - "-t"
  - name: flag-t-5
    type: number
    required: false
    default: null
    description: "the --time-stamp-precision option) between current and first line on each dump line. The default is microsecond resolution"
    aliases:
      - "-t"
  - name: flag-u
    type: string
    required: false
    default: null
    description: "Print undecoded NFS handles"
    aliases:
      - "-u"
  - name: flag-v
    type: string
    required: false
    default: null
    description: "When parsing and printing, produce (slightly more) verbose out‐"
    aliases:
      - "-v"
  - name: flag-v-2
    type: string
    required: false
    default: null
    description: "Even more verbose output. For example, additional fields are"
    aliases:
      - "-v"
  - name: flag-v-3
    type: string
    required: false
    default: null
    description: "Even more verbose output. For example, telnet SB ... SE options"
    aliases:
      - "-v"
  - name: flag-w
    type: string
    required: false
    default: null
    description: "Write the raw packets to file rather than parsing and printing them out. They can later be printed with the -r option. Stan‐ dard output is used if file is ``-''"
    aliases:
      - "-w"
  - name: flag-x
    type: string
    required: false
    default: null
    description: "When parsing and printing, in addition to printing the headers of"
    aliases:
      - "-x"
  - name: flag-x-2
    type: string
    required: false
    default: null
    description: "When parsing and printing, in addition to printing the headers of"
    aliases:
      - "-x"
  - name: flag-y
    type: string
    required: false
    default: null
    description: "--linktype=datalinktype Set the data link type to use while capturing packets (see -L) or just compiling and dumping packet-matching code (see -d) to datalinktype"
    aliases:
      - "-y"
  - name: flag-z
    type: string
    required: false
    default: null
    description: "Used in conjunction with the -C or -G options, this will make tcpdump run \" postrotate-command file \" where file is the save‐ file being closed after each rotation. For example, specifying -z gzip or -z bzip2 will compress each savefile using gzip or bzip2"
    aliases:
      - "-z"
      - "-c"
  - name: help
    type: boolean
    required: false
    description: "Print the tcpdump and libpcap version strings, print a usage mes‐"
    aliases:
      - "--help"
  - name: interface
    type: boolean
    required: false
    description: ""
    aliases:
      - "--interface"
  - name: ip_oneline
    type: boolean
    required: false
    description: ""
    aliases:
      - "--ip-oneline"
  - name: linktype
    type: boolean
    required: false
    description: ""
    aliases:
      - "--linktype"
  - name: list_data_link_types
    type: boolean
    required: false
    description: ""
    aliases:
      - "--list-data-link-types"
  - name: list_interfaces
    type: boolean
    required: false
    description: ""
    aliases:
      - "--list-interfaces"
  - name: list_time_stamp_types
    type: boolean
    required: false
    description: ""
    aliases:
      - "--list-time-stamp-types"
  - name: monitor_mode
    type: boolean
    required: false
    description: ""
    aliases:
      - "--monitor-mode"
  - name: nano
    type: boolean
    required: false
    description: "‐"
    aliases:
      - "--nano"
      - "--time-stamp-precision"
      - "--time-stamp-pre"
  - name: no_optimize
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-optimize"
  - name: no_promiscuous_mode
    type: boolean
    required: false
    description: ""
    aliases:
      - "--no-promiscuous-mode"
  - name: number
    type: string
    required: false
    default: null
    description: "Print a packet number at the beginning of the line"
    aliases:
      - "--number"
  - name: packet_buffered
    type: boolean
    required: false
    description: ""
    aliases:
      - "--packet-buffered"
  - name: print
    type: string
    required: false
    default: null
    description: "Print parsed packet output, even if the raw packets are being saved to a file with the -w flag"
    aliases:
      - "--print"
  - name: relinquish_privileges
    type: boolean
    required: false
    description: ""
    aliases:
      - "--relinquish-privileges"
  - name: snapshot_length
    type: boolean
    required: false
    description: ""
    aliases:
      - "--snapshot-length"
  - name: time_stamp_type
    type: boolean
    required: false
    description: ""
    aliases:
      - "--time-stamp-type"
  - name: tt
    type: boolean
    required: false
    description: "Print the timestamp, as seconds since January 1, 1970,  00:00:00,"
    aliases:
      - "-tt"
  - name: ttt
    type: boolean
    required: false
    description: "Print a delta (microsecond or nanosecond resolution depending  on"
    aliases:
      - "-ttt"
  - name: tttt
    type: boolean
    required: false
    description: "Print a timestamp, as hours, minutes, seconds, and fractions of a"
    aliases:
      - "-tttt"
  - name: vv
    type: boolean
    required: false
    description: "Even  more  verbose  output.   For example, additional fields are"
    aliases:
      - "-vv"
  - name: vvv
    type: boolean
    required: false
    description: "Even  more verbose output.  For example, telnet SB ... SE options"
    aliases:
      - "-vvv"
  - name: xx
    type: boolean
    required: false
    description: "When parsing and printing, in addition to printing the headers of"
    aliases:
      - "-xx"

execution:
  template: "tcpdump -r {flag-r} -b {flag-b} -B {flag-b} -c {flag-c} --count {count}"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars:
  port: port
examples:
  - description: "Display help message"
    command: "tcpdump --help"
  - description: Capture packets from a specific network interface
    command: tcpdump -i eth0
  - description: Capture only a certain number of packets
    command: tcpdump -c 10
  - description: Capture and write packets to a file for later analysis
    command: tcpdump -w capture.pcap
  - description: Read packets from a file
    command: tcpdump -r capture.pcap
  - description: Capture packets from a specific host
    command: tcpdump host 192.168.1.1
  - description: Capture packets from a specific port
    command: tcpdump port 80
  - description: Capture packets based on a specific protocol (e.g., TCP)
    command: tcpdump tcp
  - description: Capture packets and filter for HTTP traffic
    command: tcpdump 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2))
      != 0)'
  - description: Capture packets from a specific source IP
    command: tcpdump src 192.168.1.1
  - description: Capture packets to a specific destination IP
    command: tcpdump dst 192.168.1.2
  - description: Display captured packets with timestamp
    command: tcpdump -tttt
  - description: Capture packets and display with verbose output
    command: tcpdump -v
  - description: Capture packets and display with extra verbose output
    command: tcpdump -vv
  - description: Capture packets and resolve hostnames
    command: tcpdump -n
  - description: Capture packets and disable resolving hostnames
    command: tcpdump -nn
  - description: Capture packets and show link-layer headers
    command: tcpdump -e
  - description: Capture IPv6 packets
    command: tcpdump ip6
  - description: Capture packets larger than a specific size
    command: tcpdump greater 1024
install:
    - method: apt
      package_name: "tcpdump"
      commands:
        - "apt-get install -y tcpdump"
    - method: brew
      package_name: "tcpdump"
      commands:
        - "brew install tcpdump"
---


# tcpdump — Dump traffic on a network interface

## Overview

`tcpdump` is a command-line utility for dump traffic on a network interface.

## Usage

```
tcpdump -r {flag-r} -b {flag-b} -B {flag-b} -c {flag-c} --count {count}
```
