# first example: better one
type_of_product = input()

output = ""
if type_of_product == "banana" or type_of_product == "apple" or type_of_product == "kiwi" \
        or type_of_product == "cherry" \
        or type_of_product == "lemon" or type_of_product == "grapes":
    output = "fruit"
elif type_of_product == "tomato" or type_of_product == "cucumber" or type_of_product == "pepper" \
        or type_of_product == "carrot":
    output = "vegetable"
else:
    output = "unknown"

print(output)

# second example:

type_of_product = input()

if type_of_product == "banana":
    print("fruit")
elif type_of_product == "apple":
    print("fruit")
elif type_of_product == "kiwi":
    print("fruit")
elif type_of_product == "cherry":
    print("fruit")
elif type_of_product == "lemon":
    print("fruit")
elif type_of_product == "grapes":
    print("fruit")
elif type_of_product == "tomato":
    print("vegetable")
elif type_of_product == "cucumber":
    print("vegetable")
elif type_of_product == "pepper":
    print("vegetable")
elif type_of_product == "carrot":
    print("vegetable")
else:
    print("unknown")
