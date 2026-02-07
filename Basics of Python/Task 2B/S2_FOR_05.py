for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(str(i * j).rjust(4))
    print("".join(row))
