print("Hello, world!!")


def multiple_of_7_but_not_of_5(start, end):
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
    print()
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=", ")


multiple_of_7_but_not_of_5(0, 100)
