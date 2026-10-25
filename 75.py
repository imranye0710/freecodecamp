def dive(map, coordinates):
    Os = 0
    for row in map:
        for element in row:
            if element == "O":
                Os += 1

    if map[coordinates[0]][coordinates[1]] == "-":
        return "Empty"
    elif map[coordinates[0]][coordinates[1]] == "X":
        if Os > 0:
            return "Found"
        elif Os == 0:
            return "Recovered"
    elif map[coordinates[0]][coordinates[1]] == "O":
        Os -= 1
        if Os >= 1:
            return "Found"
        elif Os == 0:
            return "Recovered"
        


print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))