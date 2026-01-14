import csv
from collections import defaultdict

FAILED_THRESHOLD = 3
failed_attempts = defaultdict(int)

with open("auth_logs.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["status"] == "FAILED":
            key = (row["username"], row["ip"])
            failed_attempts[key] += 1

alerts = []
for (user, ip), count in failed_attempts.items():
    if count >= FAILED_THRESHOLD:
        alerts.append(
            f"[ALERT] Possible brute-force attack on user '{user}' from IP {ip} ({count} failed attempts)"
        )

with open("output/alerts.txt", "w") as f:
    for alert in alerts:
        f.write(alert + "\n")

print("Log analysis completed. Alerts generated.")
