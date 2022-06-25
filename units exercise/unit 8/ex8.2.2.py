"""
כתבו פונקציה שנקראת sort_prices המוגדרת כך:

def sort_prices(list_of_tuples):
הפונקציה מקבלת רשימה של טאפלים שבכל אחד פריט ומחירו.
הפונקציה מחזירה רשימה של טאפלים ממוינים על פי מחיר הפריטים שבהם מהגדול לקטן.
"""


def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=get_key, reverse=True)


def get_key(my_tuple):
    return float(my_tuple[1])


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]

    print(sort_prices(products))


if __name__ == "__main__":
    main()
