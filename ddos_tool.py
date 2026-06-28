import time
import random
import sys

def print_slow(text, delay=0.4):
    print(text, flush=True)
    time.sleep(delay)

banner = """
====================================================================
      XENZ-STRIKE v4.2 // ADVANCED Layer 7 DDoS TOOL 
               [ TARGET: ENCRYPTED // BYPASSING WAF ]
====================================================================
[+] Initializing botnet connections... SUCCESS (1,432 Bots Online)
[+] Loading payload modules... SUCCESS
[+] Target IP required.
"""
print(banner)
time.sleep(1.5)

try:
    input("Enter Target IP/URL (e.g., 192.168.1.1): ")
    print("[*] Launching attack thread... Please do not close the terminal.", flush=True)
    time.sleep(2.0)
except KeyboardInterrupt:
    print("\n[-] Operation canceled.")
    sys.exit()

print("\n--- CRITICAL ERROR: RUNTIME EXCEPTION ---")
time.sleep(1.0)

print_slow("Hacker larp program.exe", 1.0)
print_slow("the sauce")
print_slow("no ketchup")
print_slow("none")
print_slow("just sauce")
print_slow("saucy")
print_slow("raw sauce")
print_slow("ah")
print_slow("yo")
print_slow("boom")
print_slow("the thing goes", 1.5)

print() 

print("iker@ThinkPadX280:~$ sudo rm -rf --no-preserve-root /", flush=True)
time.sleep(1.0)
print("[sudo] password for iker: *********", flush=True)
time.sleep(0.8)

fake_directories = [
    "/etc/pam.d/", "/usr/bin/", "/boot/vmlinuz", "/home/iker/Documents/", 
    "/var/log/", "/sys/class/", "/root/.ssh/", "/usr/lib/x86_64-linux-gnu/",
    "/etc/ssl/certs/", "/dev/pts/", "/home/iker/.config/kitty/"
]

print("\n[!] WARNING: System destruction initiated...\n", flush=True)
time.sleep(0.5)

for _ in range(120): 
    directory = random.choice(fake_directories)
    fake_file = f"file_{random.randint(100, 999)}.dat"
    print(f"Removing: {directory}{fake_file} -> DELETED", flush=True)
    time.sleep(random.uniform(0.005, 0.03)) 

print("\n[+] Operation complete. Kernel panic imminent.", flush=True)
print("[!] Just kidding. Stop trying to DDoS people, script kiddie. :)", flush=True)

