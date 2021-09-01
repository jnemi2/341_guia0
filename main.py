def process_csv(input_data):
    """

    :param input_data: string (or list of strings) with integer, substring, and boolean separated by a comma
    :return: list (or matrix) with CSV values in their correct type
    """
    data = []
    if type(input_data) == type(data):
        for i in range(len(input_data)):
            data.append(process_csv(input_data[i]))
    else:
        data = input_data.rstrip().split(",")
        data[0] = int(data[0])
        data[2] = bool(data[2])
    return data


print(process_csv(["14,Juana Perez,True", "21,Juan,True"]))
