

text = []
print("Type 'exit' to end")
input_text = input("Type something: ")
while input_text.lower() != "exit":
    text.append(input_text.capitalize())
    input_text = input("Type something: ")

for t in text:
    print(t)