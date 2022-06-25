"""
כתבו פונקציה שנקראת who_is_missing המוגדרת כך:

def who_is_missing(file_name):
הפונקציה מקבלת כפרמטר נתיב לקובץ טקסט (מחרוזת).
הקובץ שנתיבו מועבר כארגומנט מכיל רשימת מספרים שלמים מ-1 עד n כלשהו, שאינם ממוינים, מופרדים בפסיקים, כאשר אחד המספרים ברצף נעלם (כלומר חסר מן הרשימה הממוינת).

פעולת הפונקציה who_is_missing:
א. הפונקציה מחזירה את המספר החסר ברצף (int).
ב. הפונקציה כותבת את המספר החסר ברצף לקובץ חדש שנקרא found.txt.
"""


def who_is_missing(file_name):
    """read a list of numbers from a text file and find the missing number
    :param file_name: text file
    :return: the missing number in the sequence 1-n
    """
    numbers_text = open(file_name, "r")

    numbers_list = numbers_text.read()

    numbers_text.close()

    numbers_list = numbers_list.split(",")
    numbers_list.sort()

    missing_number = -1

    for i in range(1, len(numbers_list)):
        if int(numbers_list[i - 1]) != i:
            missing_number = i
            break

    print(missing_number)

    output_file = open("found.txt", "w")
    output_file.write(str(missing_number))
    output_file.close()

    return missing_number


def main():
    who_is_missing(r"D:\Users\cijhho123456\Downloads\test.txt")


if __name__ == "__main__":
    main()
