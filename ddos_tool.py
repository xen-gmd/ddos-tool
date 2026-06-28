import time
import random
import sys

# ANSI Escape Codes for Termux/Linux styling
GREEN = "\033[0;32m"
BRIGHT_GREEN = "\033[1;32m"
RED = "\033[0;31m"
BRIGHT_RED = "\033[1;31m"
RESET = "\033[0m"

def print_slow(text, delay=0.4, color=GREEN):
    print(f"{color}{text}{RESET}", flush=True)
    time.sleep(delay)

banner = f"""{BRIGHT_GREEN}
====================================================================
      XENZ-STRIKE v4.2 // ADVANCED Layer 7 DDoS TOOL 
               [ TARGET: ENCRYPTED // BYPASSING WAF ]
====================================================================
[+] Initializing botnet connections... SUCCESS (1,432 Bots Online)
[+] Loading payload modules... SUCCESS
[+] Target IP required.{RESET}
"""
print(banner)
time.sleep(1.5)

try:
    # terminal prompts look better with standard formatting
    target = input(f"{GREEN}Enter Target IP/URL (e.g., 192.168.1.1): {RESET}")
    print(f"{GREEN}[*] Launching attack thread... Please do not close the terminal.{RESET}", flush=True)
    time.sleep(2.0)
except KeyboardInterrupt:
    print(f"\n{RED}[-] Operation canceled.{RESET}")
    sys.exit()

print(f"\n{BRIGHT_RED}--- CRITICAL ERROR: RUNTIME EXCEPTION ---{RESET}")
time.sleep(1.5)

print_slow("Hacker larp program.exe", random.uniform(1.0, 1.5))
print_slow("the sauce", random.uniform(0.3, 0.6))
print_slow("no ketchup", random.uniform(0.4, 0.7))
print_slow("none", random.uniform(0.2, 0.5))
print_slow("just sauce", random.uniform(0.5, 0.8))
print_slow("saucy", random.uniform(0.3, 0.6))
print_slow("raw sauce", random.uniform(0.4, 0.8))
print_slow("ah", random.uniform(0.2, 0.4))
print_slow("yo", random.uniform(0.2, 0.5))
print_slow("boom", random.uniform(0.6, 1.0))
print_slow("the thing goes", 1.8)

print() 

print(f"{GREEN}[ddos_tool]$ sudo rm -rf --no-preserve-root /{RESET}", flush=True)
time.sleep(1.2)
print(f"{GREEN}[sudo] password for user: *********{RESET}", flush=True)
time.sleep(1.5) 

fake_directories = [
    "/etc/pam.d/", "/usr/bin/", "/boot/vmlinuz", "/home/user/Documents/", 
    "/var/log/", "/sys/class/", "/root/.ssh/", "/usr/lib/x86_64-linux-gnu/",
    "/etc/ssl/certs/", "/dev/pts/", "/home/user/.config/kitty/"
]

print(f"\n{BRIGHT_RED}[!] WARNING: System destruction initiated...\n{RESET}", flush=True)
time.sleep(0.8)

for _ in range(120): 
    directory = random.choice(fake_directories)
    fake_file = f"file_{random.randint(100, 999)}.dat"
    print(f"{GREEN}Removing: {directory}{fake_file} -> DELETED{RESET}", flush=True)
    time.sleep(random.uniform(0.005, 0.04)) 

print(f"\n{BRIGHT_RED}[+] Operation complete. Kernel panic imminent.{RESET}", flush=True)
time.sleep(2.0) 
print(f"{BRIGHT_GREEN}[!] Just kidding. Stop trying to DDoS people, script kiddie. :){RESET}", flush=True)

