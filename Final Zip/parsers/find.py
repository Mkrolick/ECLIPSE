select = [
    "input_order",
    "first_fail",
    "smallest",
    "largest",
    "occurrence",
    "most_constrained",
]
choice = [
    "indomain_min",
    "indomain_max",
    "indomain_middle",
    "indomain_random",
    "indomain_split",
]

for s in select:
    for c in choice:
        print(f"minimize(search(AllVars, 0, {s}, {c}, complete, []), EndTime),")
