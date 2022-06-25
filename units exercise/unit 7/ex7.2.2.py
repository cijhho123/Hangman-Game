"""
כתבו פונקציה בשם numbers_letters_count המוגדרת כך:

def numbers_letters_count(my_str):
הפונקציה מקבלת כפרמטר מחרוזת.
הפונקציה מחזירה רשימה שהאיבר הראשון בה מייצג את מספר הספרות במחרוזת, והאיבר השני מייצג את מספר האותיות במחרוזת, כולל רווחים, נקודות, סימני פיסוק וכל מה שאינו ספרות.
"""


def numbers_letters_count(my_str):
    """a function that receive a string and count the amount of digits and non-digits characters
    :param my_str:
    :return:
    """
    counter_list = [0, 0]

    for i in my_str:
        if i.isdigit():
            counter_list[0] += 1

    counter_list[1] = len(my_str) - counter_list[0] #calcute the complementary amount

    return counter_list