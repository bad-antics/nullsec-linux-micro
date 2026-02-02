#!/bin/bash
# NullSec Linux Micro Builder

VERSION="1.0.0"
EDITION="${1:-station}"

echo "Building NullSec Linux Micro - ${EDITION} Edition"

# Based on Debian live-build
lb config \
    --distribution bookworm \
    --architecture amd64 \
    --binary-images iso-hybrid \
    --bootappend-live "boot=live components username=nullsec" \
    --memtest none

# Add NullSec packages
mkdir -p config/package-lists
cat > config/package-lists/nullsec.list.chroot << 'PKG'
nmap
masscan
wireshark
metasploit-framework
aircrack-ng
hashcat
john
hydra
sqlmap
nikto
gobuster
python3-impacket
bloodhound
crackmapexec
responder
bettercap
PKG

lb build

echo "Build complete: nullsec-micro-${EDITION}.iso"
