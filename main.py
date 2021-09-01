def process_csv(text):
    """

    :param text: string with integer, substring, and boolean separated by a comma
    :return: list with CSV values in their correct type
    """
    data = text.rstrip().split(",")
    data[0] = int(data[0])
    data[2] = bool(data[2])
    return data


print(process_csv("14,Juana Perez,True"))
