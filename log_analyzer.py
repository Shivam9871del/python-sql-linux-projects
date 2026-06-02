count_logs = {}
count_error = {}
total_count = 0

print("ERROR Logs:")
print("-----------")

with open("logs.txt", "r") as file:
    for line in file:
        line = line.strip()
        total_count += 1

        log_type = line.split(":")[0]

        if log_type in count_logs:
            count_logs[log_type] += 1
        else:
            count_logs[log_type] = 1

        if line.startswith("ERROR"):
            print(line)

            error_message = line.split(":")[1].strip()

            if error_message in count_error:
                count_error[error_message] += 1
            else:
                count_error[error_message] = 1

print()
print("Log Summary Report")
print("------------------")

for log_type, count in count_logs.items():
    print(log_type, ":", count)

print()
print("Total Count :", total_count)

max_freq = 0
max_freq_log_type = ""

for log_type, count in count_logs.items():
    if count > max_freq:
        max_freq = count
        max_freq_log_type = log_type

print()
print("Most Frequent Log Type:", max_freq_log_type)
print("Frequency:", max_freq)

print()
print("Error Breakdown")
print("---------------")

for error_message, count in count_error.items():
    print(error_message, ":", count)
