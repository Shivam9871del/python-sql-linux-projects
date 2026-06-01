count_logs = {}

with open("logs.txt", "r") as file:
    for line in file:
        log_type = line.split(":")[0]

        if log_type in count_logs:
            count_logs[log_type] += 1
        else:
            count_logs[log_type] = 1

for log_type, count in count_logs.items():
    print(log_type, ":", count)
