"""
כתבו פונקציה שנקראת seven_boom אשר מדמה את המשחק "שבע בום". הפונקציה מוגדרת כך:

def seven_boom(end_number):
הפונקציה מקבלת מספר שלם, end_number.
הפונקציה מחזירה רשימה בתחום המספרים 0 עד end_number כולל, כאשר מספרים מסוימים מוחלפים במחרוזת 'BOOM', אם הם עונים על אחד מהתנאים הבאים:

המספר הוא כפולה של המספר 7.
המספר מכיל את הספרה 7.
"""


def seven_boom(end_number):
    """recive a number and play the game 7-boom
    :param end_number: the upper limit
    :return: a list of the game 7-boom
    """
    list_of_7_boom = []

    for i in range(0, end_number+1):
        if i % 7 == 0 or "7" in str(i):
            list_of_7_boom.append("BOOM")
        else:
            list_of_7_boom.append(i)

    return list_of_7_boom

def main ():
    print(seven_boom(17))

if __name__ == "__main__":
    main()