def process_csv(text):
    """

    :param text: string with substrings separated by a comma
    :return: list with substrings
    """
    return text.rstrip().split(",")


print(process_csv("John,21"))
