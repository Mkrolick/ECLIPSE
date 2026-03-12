data_lines = []

with open(
    "/Users/malcolmkrolick/Documents/GitHub/ECLIPSE/Section 2/section2.data"
) as s:
    data_lines = s.readlines()

clauses = []

for line in data_lines:
    parts = line.strip().split(" ")
    lhs = parts[0].split("_")[2]
    rhs = parts[1].split("_")[2]
    clauses.append(f"S_{rhs} #>= F_{lhs},")

for clause in clauses:
    print(clause)
