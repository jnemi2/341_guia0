print("Hello, world!!")


def generate_keymap():
    keymap = {}
    for k in range(ord("a"), ord("z") + 1):
        keymap.setdefault(chr(k), k)
    return keymap


print(generate_keymap())