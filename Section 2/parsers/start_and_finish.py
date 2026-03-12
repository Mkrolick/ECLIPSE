finish_times = []
start_times = []

for i in range(1, 576):
    if i < 10:
        i = "00" + str(i)
    elif i < 100:
        i = "0" + str(i)
    else:
        i = str(i)

    finish_times.append(f"F_{i}")
    start_times.append(f"S_{i}")


finish_clause = "TaskFinishTimes = [" + ", ".join(finish_times) + "],"
start_clause = "TaskStartTimes = [" + ", ".join(start_times) + "],"

print(finish_clause)
print(start_clause)
