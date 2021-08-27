x1 = ["💀", "💀", "💀"]
x2 = ["💀", "💀", "💀"]
x3 = ["💀", "💀", "💀"]

map_x = [x1, x2, x3]

print(f"{x1}\n{x2}\n{x3}")

mark = input("Please specify your spot index: ")

row = int(mark[0])
column = int(mark[1])

# selected_mark = map_x[row - 1]
# selected_mark[column - 1] = "X"
map_x[row - 1][column -1] = "X"

print(f"{x1}\n{x2}\n{x3}")