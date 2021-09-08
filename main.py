input_text = input("Type something: ")


def count_alpha_num_symbols(text):
    alpha = 0
    num = 0
    sym = 0
    x = "hola"
    for char in text:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            num += 1
        else:
            sym += 1
    return alpha, num, sym


letters, nums, syms = count_alpha_num_symbols(input_text)
print("Your text has {} letters, {} digits and {} symbols".format(letters, nums, syms))
