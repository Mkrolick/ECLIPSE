# read from section 1 data
"""
Tasks = [
    task('Defrost sausages',     S_DS,  F_DS),
    task('Preheat grill',        S_PG,  F_PG),
    task('Dice onions',          S_DO,  F_DO),
    task('Toast buns',           S_TB,  F_TB),
    task('Grill sausages',       S_GS,  F_GS),
    task('Add condiments',       S_ASMO,F_ASMO),
    task('Grill onions',         S_GO,  F_GO),
    task('Pan-broil sausages',   S_PBS, F_PBS)
],
"""

data_lines = []

# read over the section 1 data
with open(
    "/Users/malcolmkrolick/Documents/GitHub/ECLIPSE/Section 2/section1.data"
) as s:
    data_lines = s.readlines()

data_lines = [line.split(" ")[0] for line in data_lines]

clauses = []
for data in data_lines:
    int_start = data.split("_")[2]
    name = data

    clauses.append(f"\ttask('{name}', S_{int_start}, F_{int_start}),")

print("Tasks = [")
for clause in clauses:
    print(clause)
print("]")
