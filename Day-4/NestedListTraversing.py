                    # Nested List Traversing in Python. 
# Nested List means a list inside a list. For example, a list of lists. We can traverse a nested list using a for loop.
group = [
    ["Accounting", "Finance", "HR"],
    ["IT", "Marketing", "Sales"],
    [12, 13, 14],
    ["Math", "Physics", "Chemistry"],
    ["Biology", "Zoology", "Botany"]
]

for i in group:
        # print(i)
    for j in i:
        print(j)
