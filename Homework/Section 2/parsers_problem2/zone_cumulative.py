Zone_Max_Occ = [
    ("Za", 2),
    ("Zb", 1),
    ("Zc", 1),
    ("Zd", 2),
    ("Ze", 1),
    ("Zf", 2),
    ("Zg", 1),
    ("Zh", 2),
    ("Zi", 5),
    ("Zj", 2),
    ("Zk", 1),
    ("Zl", 4),
    ("Zm", 3),
]

data_lines = []
with open(
    "/Users/malcolmkrolick/Documents/GitHub/ECLIPSE/Section 2/section1.data"
) as s:
    data_lines = [line.strip() for line in s.readlines()]

parsed_line = []
for line in data_lines:
    parts = line.strip().split(" ")
    name = parts[0]
    id = name.split("_")[2]
    time = parts[1]
    min = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
    zone_usage = [int(x) for x in parts[2 + 4 :]]

    parsed_line.append((id, min, zone_usage))

zone_names = [name for name, _ in Zone_Max_Occ]
zone_data = {z: [] for z in zone_names}

for data in parsed_line:
    for idx, zone_usage in enumerate(data[2]):
        if zone_usage > 0:
            zone_data[zone_names[idx]].append((data[0], data[1], zone_usage))

# build clause
for zone_name in zone_data.keys():
    clause = "cumulative(["

    ids = [n for (n, m, u) in zone_data[zone_name]]
    min = [m for (n, m, u) in zone_data[zone_name]]
    usage = [u for (n, m, u) in zone_data[zone_name]]
    clause += ", ".join([f"S_{id}" for id in ids]) + "], ["
    clause += ", ".join([str(m) for m in min]) + "], ["
    clause += ", ".join([str(u) for u in usage]) + "], "
    clause += str([x[1] for x in Zone_Max_Occ if x[0] == zone_name][0]) + ")"
    print(clause)
