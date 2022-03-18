students = [
    ["Electro", ["Yae", "Baal"]],
    ["Geo", ["Ningguang", "Albedo"]],
    ["Anemo", ["Jean", "Xiao"]]
]

for x in students:
    print(x[0])
    for i in x[1]:
        print(" -" + i)
    print()