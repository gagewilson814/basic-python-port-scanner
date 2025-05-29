# Basic Port Scanner (Python)

This is a simple command-line port scanner written in Python. It was created as a learning exercise to explore socket programming and get familiar with Python syntax. This tool performs a sequential scan over a given IP address and port range to identify open ports.

> ⚠️ **Warning:** This scanner is for educational purposes only. Use it **only** on networks and devices that **you own or have explicit permission to scan**. The author is **not responsible** for any misuse that leads to consequences such as triggering intrusion detection systems (IDS) on corporate or private networks.

---

## Features

- Scans a single target IP address
- Customizable port range (default: 1–65535)
- Outputs open ports to `ScanResults.txt`
- Simple and lightweight (no third-party libraries)
- Synchronous (single-threaded) for simplicity

---

## Usage

```bash
python3 scanner.py <target-ip> [<start-port> <end-port>]
```
## Limitations
- Not multi-threaded — can be slow for wide port ranges
- Timeout is set very low for speed and may result in missed ports on slower networks

## Potential future improvments
- Expand to be multi-threaded
