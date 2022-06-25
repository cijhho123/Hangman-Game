"""
כתבו פונקציה שנקראת squared_numbers המוגדרת כך:

def squared_numbers(start, stop):
הפונקציה מקבלת שני מספרים שלמים, start ו-stop (הניחו שמתקיים: start <= stop). הפונקציה מחזירה רשימה בה נמצאים כל ריבועי המספרים בין start ל-stop (כולל).
"""


def squared_numbers(start, stop):
    """a function that return a list of all the squares of the numbers from <start> to <stop> inclusive
    :param start: the lower bound
    :param stop: the upper bound
    :return: a list of all the square numbers
    """
    square_list = []
    while start <= stop:
        square_list.append(start ** 2)
        start += 1

    return square_list


def main():
    print(squared_numbers(1, 10))


if __name__ == "__main__":
    main()
