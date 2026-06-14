---
trust_level: community
id: windows-dllhijack-dwrite
namespace: windows:dllhijack:dwrite
name: dwrite.dll
description: "dwrite.dll — Sideloading hijacking (Microsoft)"
author: "Wietze Beukema"
version: "1.0.0"
capabilities:
  - security.defenseevasion.dll-hijack
platforms:
  - windows
techniques:
  - defense-evasion
  - persistence
execution:
  template: "dwrite.dll"
  sandbox: execFile
  timeout_seconds: 30
  shell: false
references:
  - label: "Reference"
    url: "https://wietze.github.io/blog/hijacking-dlls-in-windows"
  - label: "Reference"
    url: "https://ctrlaltintel.com/research/FudCrypt-analysis-1/"
  - label: "Reference"
    url: "https://code.visualstudio.com/docs/setup/windows"
  - label: "Reference"
    url: "https://slack.com/help/articles/212475728-Deploy-Slack-via-Microsoft-Installer"
  - label: "Reference"
    url: "https://www.framer.com/downloads/"
  - label: "Reference"
    url: "https://dev.evernote.com/documentation/local/chapters/windows.php"
  - label: "Reference"
    url: "https://docs.getsession.org/session-messenger/installing-session"
  - label: "Reference"
    url: "https://www.canva.com/download/windows/"
  - label: "Reference"
    url: "https://docs.element.io/latest/element-server-suite-classic/administration/configuring-element-desktop/"
  - label: "Reference"
    url: "https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-github-desktop"
  - label: "Reference"
    url: "https://gologin.com/docs/getting-started/setup/"
  - label: "Reference"
    url: "https://www.notion.com/help/deploy-notion-for-windows"
  - label: "Reference"
    url: "https://help.obsidian.md/install"
  - label: "HijackLibs"
    url: "https://hijacklibs.net/entries/dwrite.html"
---
examples:
  - description: "Place malicious dwrite.dll in the search order location"
    command: "copy malicious.dll \"%SYSTEM32%\\dwrite.dll\""
  - description: "Execute the vulnerable binary to trigger the hijack"
    command: "\"%SYSTEM32%\\cttune.exe\""

# dwrite.dll

**Vendor:** Microsoft

**Expected Location:** %SYSTEM32%

**Vulnerable Executables:**
- %SYSTEM32%\cttune.exe (Sideloading)
- %SYSTEM32%\dataexchangehost.exe (Sideloading)
- %SYSTEM32%\gamepanel.exe (Sideloading)
- %LOCALAPPDATA%\Discord\app-%VERSION%\Discord.exe (Sideloading)
- %LOCALAPPDATA%\Framer\app-%VERSION%\Framer.exe (Sideloading)
- %LOCALAPPDATA%\slack\app-%VERSION%\slack.exe (Sideloading)
- %LOCALAPPDATA%\Programs\Evernote\Evernote.exe (Sideloading)
- %LOCALAPPDATA%\Programs\Canva\Canva.exe (Sideloading)
- %LOCALAPPDATA%\Programs\Session\Session.exe (Sideloading)
- %LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe (Sideloading)
- %LOCALAPPDATA%\element-desktop\app-%VERSION%\Element.exe (Sideloading)
- %LOCALAPPDATA%\GitHubDesktop\app-%VERSION%\GitHubDesktop.exe (Sideloading)
- %LOCALAPPDATA%\Programs\GoLogin\GoLogin.exe (Sideloading)
- %LOCALAPPDATA%\Programs\Notion\Notion.exe (Sideloading)
- %PROGRAMFILES%\Obsidian\Obsidian.exe (Sideloading)

**Acknowledgement:** Wietze

**Acknowledgement:** Josh Allman
