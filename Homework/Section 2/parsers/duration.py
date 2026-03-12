data_lines = []

# read over the section 1 data
with open(
    "/Users/malcolmkrolick/Documents/GitHub/ECLIPSE/Section 2/section1.data"
) as s:
    data_lines = s.readlines()

time_durations = [
    {"name": x.split("_")[2].split(" ")[0], "time": x.split(" ")[1]} for x in data_lines
]

# Convert time
time_durations = [
    {
        "name": x["name"],
        "time": int(x["time"].split(":")[0]) * 60 + int(x["time"].split(":")[1]),
    }
    for x in time_durations
]

clauses = [f"F_{x['name']} - S_{x['name']} #= {x['time']}," for x in time_durations]

# Pipe output
for clause in clauses:
    print(clause)
