print("Hello, world!!")


def generate_keymap():
    """

    :return: dictionary with the ASCII keymap of the alphabet
    """
    keymap = {}
    for k in range(ord("a"), ord("z") + 1):
        keymap.setdefault(chr(k), k)
    return keymap


print(generate_keymap())