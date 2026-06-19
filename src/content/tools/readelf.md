---
id: dev-symbol-readelf
namespace: dev:symbol:readelf
name: readelf
description: ELF file reader, can read binary files.
author: "GTFOBins"
version: "1.0.0"
capabilities:
  - system.file.read
platforms:
  - linux
  - bsd
risk_level: low
trust_level: community
execution_policy: enabled
architectures:
  - amd64
  - arm64
dependencies: []
related_tools:
  - nm
  - objdump
artifacts: []
workflow_edges:
  produces:
    - file-content
  consumes:
    - file
contract:
  inputs: []
  outputs:
    - type: process.output
      description: File content output
  side_effects: []
  resource_cost:
    cpu: low
    memory_mb: 4
    network: none
    disk_io: low
resource_profile:
  cpu: low
  memory_mb: 4
  network: none
  disk_io: low
allowed-tools:
  - readelf
  - nm
  - Bash
  - execFile
parameters:

  - name: all
    type: string
    required: false
    default: null
    description: "Equivalent to: -h -l -S -s -r -d -V -A -I --got-contents"
    aliases:
      - "-a"
      - "--all"
  - name: arch-specific
    type: string
    required: false
    default: null
    description: "Display architecture specific information (if any)"
    aliases:
      - "-A"
      - "--arch-specific"
  - name: archive-index
    type: string
    required: false
    default: null
    description: "Display the symbol/file index in an archive"
    aliases:
      - "-c"
      - "--archive-index"
  - name: ctf
    type: string
    required: false
    default: null
    description: "Display CTF info from section <number|name>"
    aliases:
      - "--ctf"
  - name: ctf-parent
    type: string
    required: false
    default: null
    description: "Use CTF archive member <name> as the CTF parent"
    aliases:
      - "--ctf-parent"
  - name: ctf-strings
    type: string
    required: false
    default: null
    description: "Use section <number|name> as the CTF external strtab"
    aliases:
      - "--ctf-strings"
  - name: ctf-symbols
    type: string
    required: false
    default: null
    description: "Use section <number|name> as the CTF external symtab"
    aliases:
      - "--ctf-symbols"
  - name: debug-dump
    type: string
    required: false
    default: null
    description: "f/=frames, F/=frames-interp, g/=gdb_index, i/=info, o/=loc, m/=macro, p/=pubnames, t/=pubtypes, R/=Ranges, l/=rawline, s/=str, O/=str-offsets, u/=trace_abbrev, T/=trace_aranges, U/=trace_info] Display the contents of DWARF debug sections"
    aliases:
      - "-w"
      - "--debug-dump"
  - name: debug-dump-2
    type: string
    required: false
    default: null
    description: "debuginfo files"
    aliases:
      - "-w"
      - "--debug-dump"
  - name: debug-dump-3
    type: string
    required: false
    default: null
    description: "Follow links to separate debug info files (default)"
    aliases:
      - "-w"
      - "-l"
      - "--debug-dump"
  - name: debug-dump-4
    type: string
    required: false
    default: null
    description: "Do not follow links to separate debug info files"
    aliases:
      - "-w"
      - "-f"
      - "-l"
      - "--debug-dump"
  - name: decompress
    type: string
    required: false
    default: null
    description: "Decompress section before dumping it"
    aliases:
      - "-z"
      - "--decompress"
  - name: demangle
    type: string
    required: false
    default: null
    description: "STYLE can be \"none\", \"auto\", \"gnu-v3\", \"java\", \"gnat\", \"dlang\", \"rust\" --no-demangle Do not demangle low-level symbol names. (default) --recurse-limit Enable a demangling recursion limit. (default) --no-recurse-limit Disable a demangling recursion limit -U[dlexhi] --unicode=[default|locale|escape|hex|highlight|invalid] Display unicode characters as determined by the current locale (default), escape sequences, \"<hex sequences>\", highlighted escape sequences, or treat them as invalid and display as \"{hex sequences}\" -X --extra-sym-info Display extra information when showing symbols --no-extra-sym-info Do not display extra information when showing symbols (default)"
    aliases:
      - "-C"
      - "--demangle"
  - name: display-section
    type: string
    required: false
    default: null
    description: "Display the contents of the indicated section. Can be repeated"
    aliases:
      - "-j"
      - "--display-section"
  - name: dwarf-depth
    type: integer
    required: false
    default: null
    description: "Do not display DIEs at depth N or greater"
    aliases:
      - "--dwarf-depth"
  - name: dwarf-start
    type: integer
    required: false
    default: null
    description: "Display DIEs starting at offset N"
    aliases:
      - "--dwarf-start"
  - name: dyn-syms
    type: string
    required: false
    default: null
    description: "Display the dynamic symbol table"
    aliases:
      - "--dyn-syms"
  - name: dynamic
    type: string
    required: false
    default: null
    description: "Display the dynamic section (if present)"
    aliases:
      - "-d"
      - "--dynamic"
  - name: file-header
    type: string
    required: false
    default: null
    description: "Display the ELF file header"
    aliases:
      - "-h"
      - "--file-header"
  - name: got-contents
    type: string
    required: false
    default: null
    description: "Display GOT section contents"
    aliases:
      - "--got-contents"
  - name: headers
    type: string
    required: false
    default: null
    description: "Equivalent to: -h -l -S"
    aliases:
      - "-e"
      - "--headers"
  - name: help
    type: string
    required: false
    default: null
    description: "Display this information"
    aliases:
      - "-H"
      - "--help"
  - name: hex-dump
    type: string
    required: false
    default: null
    description: "Dump the contents of section <number|name> as bytes"
    aliases:
      - "-x"
      - "--hex-dump"
  - name: histogram
    type: string
    required: false
    default: null
    description: "Display histogram of bucket list lengths"
    aliases:
      - "-I"
      - "--histogram"
  - name: lint
    type: string
    required: false
    default: null
    description: "Display warning messages for possible problems"
    aliases:
      - "-L"
      - "--lint"
      - "--enable-checks"
  - name: lto-syms
    type: string
    required: false
    default: null
    description: "Display LTO symbol tables"
    aliases:
      - "--lto-syms"
  - name: no_demangle
    type: boolean
    required: false
    description: "symbol names.  (default)"
    aliases:
      - "--no-demangle"
      - "-level"
  - name: no_extra_sym_info
    type: boolean
    required: false
    description: "Do not display extra information when showing symbols (default)"
    aliases:
      - "--no-extra-sym-info"
  - name: no_recurse_limit
    type: boolean
    required: false
    description: "Disable a demangling recursion limit"
    aliases:
      - "--no-recurse-limit"
  - name: notes
    type: string
    required: false
    default: null
    description: "Display the contents of note sections (if present)"
    aliases:
      - "-n"
      - "--notes"
  - name: process-links
    type: string
    required: false
    default: null
    description: "Display the contents of non-debug sections in separate"
    aliases:
      - "-P"
      - "--process-links"
  - name: program-headers
    type: string
    required: false
    default: null
    description: "Display the program headers"
    aliases:
      - "-l"
      - "--program-headers"
  - name: recurse_limit
    type: boolean
    required: false
    description: "Enable a demangling recursion limit.  (default)"
    aliases:
      - "--recurse-limit"
  - name: relocated-dump
    type: string
    required: false
    default: null
    description: "Dump the relocated contents of section <number|name>"
    aliases:
      - "-R"
      - "--relocated-dump"
  - name: relocs
    type: string
    required: false
    default: null
    description: "Display the relocations (if present)"
    aliases:
      - "-r"
      - "--relocs"
  - name: section-details
    type: string
    required: false
    default: null
    description: "Display the section details"
    aliases:
      - "-t"
      - "--section-details"
  - name: section-groups
    type: string
    required: false
    default: null
    description: "Display the section groups"
    aliases:
      - "-g"
      - "--section-groups"
  - name: section-headers
    type: string
    required: false
    default: null
    description: "Display the sections' header"
    aliases:
      - "-S"
      - "--section-headers"
  - name: sections
    type: string
    required: false
    default: null
    description: "An alias for --section-headers"
    aliases:
      - "--sections"
  - name: segments
    type: string
    required: false
    default: null
    description: "An alias for --program-headers"
    aliases:
      - "--segments"
  - name: sframe
    type: string
    required: false
    default: null
    description: "Display SFrame info from section NAME, (default '.sframe')"
    aliases:
      - "--sframe"
  - name: silent-truncation I
    type: string
    required: false
    default: null
    description: ""
    aliases:
      - "-T"
      - "--silent-truncation I"
  - name: string-dump
    type: string
    required: false
    default: null
    description: "Dump the contents of section <number|name> as strings"
    aliases:
      - "-p"
      - "--string-dump"
  - name: sym-base
    type: string
    required: false
    default: null
    description: "Force base for symbol sizes. The options are mixed (the default), octal, decimal, hexadecimal"
    aliases:
      - "--sym-base"
  - name: symbols
    type: string
    required: false
    default: null
    description: "An alias for --syms"
    aliases:
      - "--symbols"
  - name: syms
    type: string
    required: false
    default: null
    description: "Display the symbol table"
    aliases:
      - "-s"
      - "--syms"
  - name: unwind
    type: string
    required: false
    default: null
    description: "Display the unwind info (if present)"
    aliases:
      - "-u"
      - "--unwind"
  - name: use-dynamic
    type: string
    required: false
    default: null
    description: "Use the dynamic section info when displaying symbols"
    aliases:
      - "-D"
      - "--use-dynamic"
  - name: version
    type: integer
    required: false
    default: null
    description: "Display the version number of readelf"
    aliases:
      - "-v"
      - "--version"
  - name: version-info
    type: string
    required: false
    default: null
    description: "Display the version sections (if present)"
    aliases:
      - "-V"
      - "--version-info"
  - name: wK
    type: boolean
    required: false
    description: ""
    aliases:
      - "-wK"
      - "--debug-dump"
      - "-links"
  - name: wN
    type: boolean
    required: false
    description: ""
    aliases:
      - "-wN"
      - "--debug-dump"
      - "-follow-links"
  - name: wide
    type: string
    required: false
    default: null
    description: "Allow output width to exceed 80 characters"
    aliases:
      - "-W"
      - "--wide"
  - name: wk
    type: boolean
    required: false
    description: "Display the contents of sections that link to separate"
    aliases:
      - "-wk"
      - "--debug-dump"

features:
  - file-system
execution:
  template: "readelf -a /path/to/binary"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
global_vars: {}
examples:
  - description: Read an ELF file via readelf
    command: readelf -a /path/to/binary
references:
  - label: "GTFOBins"
    url: "https://gtfobins.github.io/gtfobins/readelf/"
techniques:
  - collection
install:
  - method: apt
    package_name: "binutils"
    commands:
      - "apt-get install -y binutils"
---
