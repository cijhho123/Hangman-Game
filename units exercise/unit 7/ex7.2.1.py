"""
כתבו פונקציה בשם is_greater המוגדרת כך:

def is_greater(my_list, n):
הפונקציה מקבלת שני פרמטרים: רשימה ומספר n.
הפונקציה מחזירה רשימה חדשה ובה כל האיברים שגדולים מהמספר n.
"""


def is_greater(my_list, n):
    """a function that take a list and a number, and return a new list with all the numberes greater than n in the list
    :param my_list: list of numbers
    :param n: the numbers all the numbers in the llist should be greater of
    :return: the new list
    """
    new_list = []
    for i in my_list:
        if i > n:
            new_list.append(i)

    return new_list
