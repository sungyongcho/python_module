import random
# ref:
# https://stackoverflow.com/questions/27437363/how-do-you-create-a-program-that-shuffles-a-list-without-using-the-shuffle-fun


def list_randomizer(lst):
    result = []
    while len(lst) > 0:
        index = random.randrange(0, len(lst))
        result.append(lst.pop(index))
    return result


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) or (not (option == "shuffle" or
                                          option == "unique" or
                                          option == "ordered" or
                                          option is None)):
        yield "ERROR"
    else:
        if option is None:
            split_list = text.split(sep)
        elif option == "shuffle":
            split_list = list_randomizer(list(text.split(sep)))
        elif option == "unique":
            split_list = list(dict.fromkeys(text.split(sep)))
        elif option == "ordered":
            split_list = sorted(text.split(sep))
        for item in split_list:
            yield item


if __name__ == '__main__':

    TEXT = "Le Lorem Ipsum est simplement du faux texte."

    print("# Regular")
    for word in generator(TEXT, sep=" "):
        print(word)
    print()

    print("# Shuffle")
    for word in generator(TEXT, sep=" ", option="shuffle"):
        print(word)
    print()

    print("# Ordered")
    for word in generator(TEXT, sep=" ", option="ordered"):
        print(word)
    print()

    unique = "Lorem Ipsum Lorem Ipsum"
    print("# Unique")
    for word in generator(unique, sep=" ", option="unique"):
        print(word)
    print()

    not_working = 1.0

    for word in generator(not_working, sep="."):
        print(word)
