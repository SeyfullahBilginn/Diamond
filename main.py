alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"];
input = "E"

index = alphabet.index(input)

arr = alphabet[1:index] + alphabet[index:0:-1]

total = index*2 + 1
edge = index - 1

print(" "*index + "A" + " "*index)
for i in arr:
    print(" " *abs(edge) + i + " " * (total - 2 * abs(edge) - 2) + i + " " * abs(edge))
    edge = edge - 1
print(" " * index + "A" + " " * index)
