from collections import defaultdict

log_file = "auth.log"
failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from")[1].strip()
            failed_attempts[ip] += 1

print("Suspicious IPs:")
for ip, count in failed_attempts.items():
    if count >= 2:
        print(f"{ip} → {count} failed attempts")