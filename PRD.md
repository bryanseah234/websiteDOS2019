# PRD: websiteDOS2019

## Overview
A Python educational script demonstrating a simple Denial-of-Service (DoS) attack using TCP socket flooding. Opens multiple threads that each continuously send HTTP GET requests to a target. Published in 2019 for educational purposes to illustrate how DoS attacks work at the socket level.

## Goals
- Demonstrate the mechanics of a TCP-based HTTP flood DoS attack
- Show how multi-threading amplifies connection rate
- Serve as educational material for network security courses

## Non-Goals
- Production-ready attack tooling
- Distributed (DDoS) coordination
- Evasion techniques
- Any legitimate use case beyond education

## User Stories
- As a security student, I want to understand what a basic DoS attack looks like in code.
- As a CTF participant, I want to test a simple flood against a local test environment I control.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `socket` (stdlib), `threading` (stdlib)

## Architecture
```
websiteDOS2019/
├── ddos.py     # main attack script
└── ddos.pyw    # same script, hidden-window version
```

**Logic:**
1. Define `target` IP, `fake_ip`, `port`
2. `attack()` function: infinite loop — open TCP socket, send malformed HTTP GET, increment counter, close
3. Spawn 500 threads (range(500) per line, but comment says "500 threads") each running `attack()`

Note: the code currently creates 5 threads (`for i in range(5)`) — comment says 500 but range is 5.

## Features

### TCP Flood
- Opens `socket.AF_INET`, `SOCK_STREAM` connection per request
- Sends raw HTTP GET with spoofed Host header
- Reconnects immediately after close (infinite loop per thread)
- Counts and prints total attack number across all threads

## Data / Config
Hardcoded constants at top of script:
| Var | Default | Description |
|-----|---------|-------------|
| `target` | `'0.0.0.0'` | Target IP — must be changed by user |
| `fake_ip` | `'0.0.0.0'` | Spoofed host header IP |
| `port` | `80` | Target port |

## Deployment / Run
```bash
python ddos.py
```

## Constraints & Notes
- **LEGAL**: Launching this against any system you do not own or have explicit written permission to test is a criminal offense under computer crime laws worldwide (e.g., CFAA in US, Computer Misuse Act in SG). Do not use on real targets.
- **Effectiveness**: Modern servers with rate limiting, firewalls, or CDNs will not be affected by 5 threads
- **IP spoofing**: The `fake_ip` only spoofs the HTTP Host header, not the actual TCP source IP — this is not real IP spoofing
- **Thread count discrepancy**: comment says 500 threads but `range(5)` creates 5
- **No cleanup**: threads run forever; must `Ctrl+C` to stop
