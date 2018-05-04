import time

log_path = "/var/log/auth.log"

while True:
    failed_attempts = []
    with open(log_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "Failed" in line:
            failed_attempts.append(line)
            #print(line)

    print(len(failed_attempts))

    msg = 'Csiga VPS - Faied SSH login attempts this week: {}'.format(len(failed_attempts))

    time.sleep(86400)