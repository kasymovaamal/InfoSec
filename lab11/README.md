# Lab 11: Installing Packages from Source

Performed inside a Docker Ubuntu container (`docker run -it --name lab11 ubuntu bash`).

## youtube-dl (setup.py-based install)
- Installed dependencies: `apt install -y python3 python3-pip python3-setuptools`
- Cloned: `git clone https://github.com/ytdl-org/youtube-dl.git`
- Installed: `python3 setup.py install`
- Verified: `youtube-dl --version` → confirmed version 2025.4.7

## neofetch (git + make install)
- Installed dependencies: `apt install -y git make`
- Cloned: `git clone https://github.com/dylanaraps/neofetch.git`
- Installed: `make install`
- Verified: `neofetch` → displayed system info with ASCII art

## Task: fzf (automated install script method)
- Cloned: `git clone --depth 1 https://github.com/junegunn/fzf.git`
- Ran the automated installer: `./install`
- Install script built the binary (`bin/fzf`) but didn't complete shell/PATH integration
- Verified directly: `./bin/fzf --version`
- Copied binary to make it globally available: `cp bin/fzf /usr/local/bin/`
- Tested interactively: `find / -type f 2>/dev/null | fzf` — opened a fuzzy file search

## Findings
Different projects use different install conventions depending on their ecosystem — Python packages often use `setup.py install`, C/Bash-based CLI tools commonly use `make install` via a Makefile, and many modern tools ship a self-contained install script. These scripts don't always finish every step automatically (e.g. fzf's installer built the binary but skipped linking it into PATH) — checking the output directory (`bin/`, `src/`, etc.) is a useful fallback when a tool doesn't show up as a global command after install.
