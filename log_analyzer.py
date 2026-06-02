count_logs = {}
count_error = {}
total_count = 0
max_freq = 0
max_freq_log_type = ""

with open("logs.txt", "r") as file:
    for line in file:
        total_count += 1
        log_type = line.split(":")[0]

        if log_type in count_logs:
            count_logs[log_type] += 1
        else:
            count_logs[log_type] = 1
for log_type, count in count_logs.items():
    print(log_type, ":", count)
print()
print("Total count :", total_count)
print()
for log_type, count in count_logs.items():
    if count > max_freq:
        max_freq = count
        max_freq_log_type = log_type
print ("Most frequent log_type:", max_freq_log_type)
print ("Frequency:", max_freq)
print()
with open("logs.txt", "r") as file:
    for line in file:
        if line.startswith("ERROR"):
            print(line, end ="")
print()
with open("logs.txt", "r") as file:
    for line in file:
        if line.startswith("ERROR"):
            error_message = line.split(":")[1].strip()

            if error_message in count_error:
                count_error[error_message] += 1
            else:
                count_error[error_message] = 1

for error_message, count1 in count_error.items():
    print(error_message, ":", count1)
