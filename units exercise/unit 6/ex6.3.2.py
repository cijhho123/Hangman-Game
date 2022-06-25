"""
כתבו פונקציה בשם longest המוגדרת כך:

def longest(my_list):
הפונקציה מקבלת רשימה המורכבת ממחרוזות ומחזירה את המחרוזת הארוכה ביותר.

הנחיות
אין להשתמש בלולאות.
"""


def longest(my_list):
    """return the longest string in the list
    :param my_list: list of strings
    :return: the longest string found in the list
    """
    my_list.sort(key=len)
    return my_list[-1]


def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == "__main__":
    main()
