"""
כתבו פונקציה בשם format_list המוגדרת כך:

def format_list(my_list):
הפונקציה מקבלת רשימת מחרוזות באורך זוגי. הפונקציה מחזירה מחרוזת המכילה את איברי הרשימה במיקומים הזוגיים, מופרדים בפסיק ורווח, ובנוסף גם את האיבר האחרון עם הכיתוב and לפניו.

הנחיות
אין להשתמש בלולאות.
"""

def format_list(my_list):
    """a function that recive a list of strings and return a string of all the concatenated strings separated by a comma
    :param my_list: list of string
    :return: the concatenated string
    """
    return ', '.join(my_list[0: : 2]) + ", and " + my_list[-1]

def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

if __name__ == "__main__":
    main()