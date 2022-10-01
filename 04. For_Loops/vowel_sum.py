text = input()
suma = 0

for char in range(0, len(text)):
    if text[char] == "a":
        suma += 1
    if text[char] == "e":
        suma += 2
    if text[char] == "i":
        suma += 3
    if text[char] == "o":
        suma += 4
    if text[char] == "u":
        suma += 5
print(suma)
