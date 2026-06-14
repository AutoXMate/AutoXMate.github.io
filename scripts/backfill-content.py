#!/usr/bin/env python3
"""
AutoXMate Content Backfill
Backfills missing frontmatter fields for tools where we can infer them safely:
  - install: based on namespace/domain and tool name
  - features: based on namespace and capabilities
  - detections: for security tools (disabled by default -- use --detections)

Runs in --dry-run mode by default. Use --apply to write changes.
"""

import os
import sys
import re
import yaml
import json
import argparse
from pathlib import Path
from collections import defaultdict

TOOLS_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "tools"


def load_tool(filename):
    """Parse a tool markdown file and return (frontmatter_dict, body_md)."""
    fpath = TOOLS_DIR / filename
    if not fpath.exists():
        return None, None
    content = fpath.read_text(encoding="utf-8", errors="replace")
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)', content, re.DOTALL)
    if not fm_match:
        return None, content
    try:
        data = yaml.safe_load(fm_match.group(1))
    except yaml.YAMLError:
        return None, content
    return data if isinstance(data, dict) else None, fm_match.group(2)


def dump_frontmatter(data):
    """Serialize dict back to YAML frontmatter as a string."""
    return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True).strip()


# ─── KNOWN PACKAGE MAPPINGS ───

KNOWN_APT = {
    "7z": "p7zip-full", "ab": "apache2-utils", "amass": "amass",
    "ansible": "ansible", "apache2": "apache2", "aria2c": "aria2",
    "arp": "net-tools", "arp-scan": "arp-scan", "at": "at",
    "awk": "gawk", "bandwhich": "bandwhich", "bat": "batcat",
    "bc": "bc", "bfs": "bfs", "bind": "bind9", "binwalk": "binwalk",
    "bpftrace": "bpftrace", "broot": "broot", "btop": "btop",
    "bzip2": "bzip2", "cadaver": "cadaver", "caddy": "caddy",
    "cal": "bsdmainutils", "calc": "bc", "cfdisk": "util-linux",
    "chaos": "chaos", "chattr": "e2fsprogs", "chmod": "coreutils",
    "chown": "coreutils", "chromium": "chromium", "cifs": "cifs-utils",
    "cksum": "coreutils", "cmp": "diffutils", "colordiff": "colordiff",
    "comm": "coreutils", "compose": "docker-compose", "cp": "coreutils",
    "cpio": "cpio", "crackmapexec": "crackmapexec", "croc": "croc",
    "cron": "cron", "cryptsetup": "cryptsetup", "csplit": "coreutils",
    "csvtool": "csvtool", "curl": "curl", "cut": "coreutils",
    "date": "coreutils", "dc": "dc", "dd": "coreutils",
    "df": "coreutils", "diff": "diffutils", "dig": "dnsutils",
    "dirb": "dirb", "dirname": "coreutils", "dirsearch": "dirsearch",
    "dmesg": "util-linux", "dnschef": "dnschef", "dnsrecon": "dnsrecon",
    "dnswalk": "dnswalk", "docker": "docker.io", "dos2unix": "dos2unix",
    "dpkg": "dpkg", "du": "coreutils", "dub": "dub",
    "dusage": "dusage", "dust": "dust", "efibootmgr": "efibootmgr",
    "eog": "eog", "ethtool": "ethtool", "exa": "exa",
    "exiftool": "libimage-exiftool-perl", "expand": "coreutils",
    "expect": "expect", "expr": "coreutils", "factor": "coreutils",
    "fdupes": "fdupes", "feroxbuster": "feroxbuster",
    "ffmpeg": "ffmpeg", "ffuf": "ffuf", "fibr": "fibr",
    "file": "file", "find": "findutils", "finger": "finger",
    "flameshot": "flameshot", "flock": "util-linux",
    "fmt": "coreutils", "fold": "coreutils", "free": "procps",
    "fuser": "psmisc", "fzf": "fzf", "gau": "gau",
    "gcc": "gcc", "gdb": "gdb", "getfacl": "acl",
    "gh": "gh", "ghidra": "ghidra", "git": "git",
    "gzip": "gzip", "hashcat": "hashcat", "hd": "xxd",
    "head": "coreutils", "host": "dnsutils", "htop": "htop",
    "httpie": "httpie", "httpx": "httpx", "hydra": "hydra",
    "ifconfig": "net-tools", "imagemagick": "imagemagick",
    "iperf3": "iperf3", "iwconfig": "wireless-tools",
    "jq": "jq", "kubectl": "kubectl", "ldapsearch": "ldap-utils",
    "lftp": "lftp", "ln": "coreutils", "logrotate": "logrotate",
    "lorem": "lorem", "lshw": "lshw", "lsof": "lsof",
    "ltrace": "ltrace", "lua": "lua5.4", "luajit": "luajit",
    "lynx": "lynx", "lz4": "lz4", "lzop": "lzop",
    "make": "build-essential", "masscan": "masscan",
    "mc": "mc", "md5sum": "coreutils", "mdadm": "mdadm",
    "mdcat": "mdcat", "micro": "micro", "mitmproxy": "mitmproxy",
    "mkdir": "coreutils", "mktemp": "coreutils", "more": "util-linux",
    "mount": "mount", "mpv": "mpv", "msfconsole": "metasploit-framework",
    "multipass": "multipass", "mv": "coreutils", "nano": "nano",
    "nc": "netcat-openbsd", "ncdu": "ncdu", "neofetch": "neofetch",
    "netcat": "netcat-openbsd", "nftables": "nftables",
    "nginx": "nginx", "nice": "coreutils", "nikto": "nikto",
    "nmap": "nmap", "node": "nodejs", "nohup": "coreutils",
    "nslookup": "dnsutils", "nuclei": "nuclei", "numactl": "numactl",
    "od": "coreutils", "openssl": "openssl", "openssh": "openssh-server",
    "p7zip": "p7zip-full", "pacat": "pulseaudio-utils",
    "passwd": "passwd", "paste": "coreutils", "patch": "patch",
    "pathchk": "coreutils", "pbcopy": "xclip", "pbpaste": "xclip",
    "pdfimages": "poppler-utils", "pdftotext": "poppler-utils",
    "perl": "perl", "pgrep": "procps", "php": "php-cli",
    "pidstat": "sysstat", "ping": "iputils-ping", "pinky": "coreutils",
    "pip": "python3-pip", "pkg-config": "pkg-config",
    "pkill": "procps", "pstree": "psmisc", "ps": "procps",
    "pv": "pv", "pwdx": "procps", "python3": "python3",
    "qrencode": "qrencode", "rclone": "rclone",
    "redshift": "redshift", "rename": "rename",
    "resize2fs": "e2fsprogs", "responder": "responder",
    "rev": "coreutils", "rg": "ripgrep", "ripgrep": "ripgrep",
    "rlwrap": "rlwrap", "rm": "coreutils", "rmdir": "coreutils",
    "rsync": "rsync", "ruby": "ruby", "rustc": "rustc",
    "s-tui": "s-tui", "s3cmd": "s3cmd", "sar": "sysstat",
    "sass": "sass", "scp": "openssh-client", "screen": "screen",
    "sdiff": "diffutils", "sed": "sed", "seq": "coreutils",
    "setfacl": "acl", "sftp": "openssh-client",
    "sha1sum": "coreutils", "sha256sum": "coreutils",
    "shred": "coreutils", "shuf": "coreutils", "sleep": "coreutils",
    "sl": "sl", "smbclient": "smbclient", "socat": "socat",
    "sort": "coreutils", "sox": "sox", "sponge": "moreutils",
    "sqlmap": "sqlmap", "sqlite3": "sqlite3", "sqsh": "sqsh",
    "ssh": "openssh-client", "ssh-keygen": "openssh-client",
    "sshfs": "sshfs", "sshpass": "sshpass", "stat": "coreutils",
    "stdbuf": "coreutils", "strace": "strace", "strings": "binutils",
    "stty": "coreutils", "su": "coreutils", "subfinder": "subfinder",
    "sudo": "sudo", "sum": "coreutils", "syncthing": "syncthing",
    "tac": "coreutils", "tail": "coreutils", "tar": "tar",
    "tcpdump": "tcpdump", "tee": "coreutils", "telnet": "telnet",
    "test": "coreutils", "theharvester": "theharvester",
    "timeout": "coreutils", "tmux": "tmux",
    "toilet": "toilet", "top": "procps",
    "touch": "coreutils", "tr": "coreutils", "tracepath": "iputils-tracepath",
    "tree": "tree", "tshark": "tshark", "tsort": "coreutils",
    "tty": "coreutils", "ttyplot": "ttyplot", "tune2fs": "e2fsprogs",
    "ulimit": "bash", "umount": "mount",
    "uniq": "coreutils", "unlink": "coreutils",
    "unshare": "util-linux", "unxz": "xz-utils",
    "unzip": "unzip", "updatedb": "locate", "uptime": "procps",
    "users": "coreutils", "valgrind": "valgrind",
    "vim": "vim", "virt-what": "virt-what",
    "vivid": "vivid", "vmstat": "procps", "w": "procps",
    "wadl": "wadl", "watch": "procps", "wc": "coreutils",
    "wget": "wget", "whatis": "man-db", "who": "coreutils",
    "whoami": "coreutils", "wireshark": "wireshark",
    "xargs": "findutils", "xxd": "xxd", "xz": "xz-utils",
    "yes": "coreutils", "yt-dlp": "yt-dlp", "zcat": "gzip",
    "zsh": "zsh", "zstd": "zstd", "zypper": "zypper",
}

# Tools that are abuse techniques, not standalone installable tools
ABUSE_TOOLS = {
    "argument-injection", "gtfobins", "lolbin", "lolbas", "living-off",
}

SKIP_PREFIXES = ("argument-injection-", "lolbin-", "lolbas-")


def infer_install(data, filename):
    """Infer install method(s) from namespace, name, and description."""
    name = data.get("name", "")
    namespace = data.get("namespace", "")
    ns_prefix = namespace.split(":")[0] if namespace else ""
    tool_id = data.get("id", "")
    tool_name = filename.replace(".md", "")

    installs = []

    # Only backfill for Linux/macOS tools with known apt packages or common tools
    if ns_prefix == "windows" or "windows" in namespace:
        return None  # Skip Windows-native tools

    # Skip abuse/LOL techniques
    if any(tool_name.startswith(p) for p in SKIP_PREFIXES):
        return None
    if any(abuse in tool_id for abuse in ["injection", "gtfobins", "lolbas", "lolbin"]):
        return None

    # Check if tool is in our known apt mapping
    if tool_name in KNOWN_APT:
        pkg = KNOWN_APT[tool_name]
        installs.append({
            "method": "apt",
            "package_name": pkg,
            "commands": [f"apt-get install {pkg}"]
        })
        return installs

    # For Linux domain tools not in our mapping, still suggest apt
    if ns_prefix in ("system", "network", "shell", "text", "process", "runtime", "editor",
                     "archive", "compression", "image", "audio", "multimedia", "monitoring",
                     "build", "dev", "database", "crypto", "math", "encode", "package",
                     "security", "cache", "config", "document", "backup", "storage",
                     "cloud", "orchestration", "virtualization", "mail", "lang"):
        installs.append({
            "method": "apt",
            "package_name": tool_name,
            "commands": [f"apt-get install {tool_name}"]
        })
        return installs

    return None


# Features inference
FEATURE_KEYWORDS = {
    "network-intensive": ["network", "http", "tcp", "udp", "connect", "download", "upload", "scan",
                          "curl", "wget", "nmap", "ping", "ssh", "ftp", "smtp"],
    "file-system": ["file", "archive", "compress", "extract", "read", "write", "backup",
                    "tar", "zip", "gzip", "cp", "mv", "rm", "mkdir"],
    "process-manip": ["process", "run", "execute", "spawn", "terminal", "signal", "kill",
                      "ps", "top", "htop", "systemctl", "service"],
    "pipes-stdin": ["filter", "transform", "convert", "stream", "xargs",
                    "awk", "sed", "grep", "cut", "sort", "uniq"],
    "pipes-stdout": ["output", "print", "display", "list",
                     "cat", "echo", "printf", "head", "tail", "less"],
    "output-json": ["json", "--json", "-o json", "format json"],
    "streaming": ["stream", "tail -f", "journalctl -f", "monitor", "watch"],
    "interactive": ["interactive", "shell", "vim", "nano", "htop", "less",
                    "screen", "tmux", "python", "node"],
    "encryption": ["encrypt", "decrypt", "cipher", "gpg", "openssl", "certificate"],
    "compression": ["compress", "decompress", "gzip", "bzip2", "xz", "zip", "tar"],
    "stealth": ["hide", "stealth", "covert", "inject", "bypass", "evade"],
    "local": ["local", "file", "disk", "mount"],
    "remote": ["remote", "connect", "client", "server", "proxy"],
    "requires-root": ["sudo", "root", "privilege", "suid"],
    "batch": ["batch", "loop", "cron", "scheduled"],
}


def infer_features(data, filename):
    """Infer features from namespace, capabilities, and description."""
    namespace = data.get("namespace", "")
    description = data.get("description", "").lower()
    capabilities = [c.lower() for c in data.get("capabilities", [])]
    tool_id = data.get("id", "").lower()

    inferred = set()
    text = f"{namespace} {description} {' '.join(capabilities)}"

    for feature, keywords in FEATURE_KEYWORDS.items():
        for kw in keywords:
            if kw in text or kw in tool_id:
                inferred.add(feature)
                break

    return sorted(inferred)


def backfill_tool(filename, dry_run=True, target_fields=None):
    """Backfill missing fields for a single tool."""
    if target_fields is None:
        target_fields = {"features", "install"}
    data, body = load_tool(filename)
    if data is None:
        return None
    
    changes = {}
    
    # Backfill features
    if "features" in target_fields and ("features" not in data or not data.get("features")):
        inferred = infer_features(data, filename)
        if inferred:
            changes["features"] = inferred
    
    # Backfill install
    if "install" in target_fields and ("install" not in data or not data.get("install")):
        inferred = infer_install(data, filename)
        if inferred:
            changes["install"] = inferred
    
    if not changes:
        return None
    
    if dry_run:
        for field, val in changes.items():
            if isinstance(val, list):
                print(f"  [{filename}] +{field}: {len(val)} items")
            else:
                print(f"  [{filename}] +{field}: {val}")
        return "[DRY RUN] would modify"
    
    # Apply changes
    data.update(changes)
    new_fm = dump_frontmatter(data)
    new_content = f"---\n{new_fm}\n---\n\n{body.strip()}\n"
    fpath = TOOLS_DIR / filename
    fpath.write_text(new_content, encoding="utf-8")
    fields = ", ".join(changes.keys())
    return f"[OK] {filename}: added {fields}"


def main():
    parser = argparse.ArgumentParser(description="Backfill missing frontmatter fields")
    parser.add_argument("--apply", action="store_true", help="Actually write changes")
    parser.add_argument("--limit", type=int, default=0, help="Max files to process (0 = all)")
    parser.add_argument("--fields", type=str, default="features,install",
                        help="Comma-separated fields to backfill (features,install)")
    args = parser.parse_args()

    target_fields = set(args.fields.split(","))

    md_files = sorted(TOOLS_DIR.glob("*.md"))
    total = len(md_files)
    changed = 0

    mode = "DRY RUN" if not args.apply else "APPLYING"
    print(f"AutoXMate Content Backfill ({mode})")
    print(f"Target fields: {', '.join(target_fields)}")
    print(f"Total tools: {total}\n")

    for i, fpath in enumerate(md_files):
        if args.limit and i >= args.limit:
            break

        filename = fpath.name
        if filename in ("index.md",):
            continue

        result = backfill_tool(filename, dry_run=not args.apply, target_fields=target_fields)
        if result:
            changed += 1
            if args.apply:
                print(result)

    print(f"\n{'='*50}")
    print(f"Summary: {changed} modified (out of {total})")
    if not args.apply:
        print(f"Run with --apply to write changes")


if __name__ == "__main__":
    main()
