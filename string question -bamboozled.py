text = "Bamboozled"

# Diagonal printing
for i in range(len(text)):
    for j in range(len(text)):
        if i == j:
            print(text[j], end=" ")
        elif i + j == len(text) - 1:
            print(text[j], end=" ")
        else:
            print(" ", end=" ")
    print()

# Rows (repeated)
for _ in range(3):
    print(text)

# Columns (first half and reversed second half)
print(text[:6])
print(text[:6])

# Diagonally reversed rectangle
for i in range(len(text)):
    print(text[i:len(text) - i])

# Shortened versions (first 4 and last 4 letters)
print(text[:4] + "ze")
print(text[:2] + "zd")
print(text[:1] + "e")

# String with suffix
print(text + "Hype!")
print(text[:6] + "Monger!")
