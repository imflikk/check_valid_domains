import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len(sys.argv) != 2:
    print("\nMissing input file.  Please see usage below.")
    print("""
    Usage:      python3 check_domains.py <list of domains>
    Example:    python3 check_domains.py domains.txt
    """)
    sys.exit(0)

DOMAINS_FILE = sys.argv[1]

valid_domains = []

with open(DOMAINS_FILE, 'r') as f:
    print(f"[*] Reading starting list of domains from '{DOMAINS_FILE}'...\n")

    domains = f.readlines()

    for domain in domains:
        try:
            r = requests.get("http://" + domain.strip(), timeout=2, verify=False)
            valid_domains.append(domain.strip())
        except:
            continue

print("----------Valid Domains----------")

with open('valid-domains.txt', 'w') as f:
    for domain in valid_domains:
        print(domain.strip())
        f.write(domain.strip() + "\n")



print()
print("[+] Saved list of valid domains to 'valid-domains.txt'")
