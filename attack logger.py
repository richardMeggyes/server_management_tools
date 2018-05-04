import time

log_path = "/var/log/auth.log"

today = time.strftime('%b %d', time.gmtime(time.time()))
today = today.replace('0', ' ')

failed_attempts = []
with open(log_path, "r") as f:
    lines = f.readlines()

for line in lines:
    if "Failed password" in line:
        if today in line:
            failed_attempts.append(line)
            #print(line)

print(len(failed_attempts))

msg = 'Csiga VPS - Faied SSH login attempts this week: {}'.format(len(failed_attempts))

