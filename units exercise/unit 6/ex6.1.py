"""
כתבו פונקציה שנקראת shift_left. הפונקציה מקבלת רשימה באורך 3 ומחזירה רשימה חדשה מוזזת צעד אחד שמאלה.
"""


def shift_left(my_list):
    """a function that shifts a list to the left
    :param my_list: the given list
    :return: the shifted list
    """
    return [my_list[1], my_list[2], my_list[0]]


def main():
    print("ok")

    lst = [0, 1, 2]
    print("current list: ", lst)

    lst = shift_left(lst)
    print("new list: ", lst)


if __name__ == "__main__":
    main()
