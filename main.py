input_text = input("Type something: ")

my_set = set()
for word in input_text.split(" "):
    my_set.add(word.lower())

print(my_set)
