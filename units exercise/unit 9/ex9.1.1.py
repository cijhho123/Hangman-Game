"""
כתבו פונקציה שנקראת are_files_equal המוגדרת כך:

def are_files_equal(file1, file2):
הפונקציה מקבלת כפרמטרים נתיבים של שני קבצי טקסט (מחרוזות).

הפונקציה מחזירה אמת (True) אם הקבצים זהים בתוכנם, אחרת מחזירה שקר (False).
"""


def are_files_equal(file1, file2):
    """check if two text filles are the same
    :param file1: first the file
    :param file2: second text file
    :return: true - same        false - not the same
    """
    file_object1 = open(file1, "r")
    file_object2 = open(file2, "r")

    str1 = file_object1.read()
    str2 = file_object2.read()

    file_object1.close()
    file_object2.close()

    return str1 == str2


def main():
    a = "hello"
    b = "hello"
    print(a == b)


if __name__ == "__main__":
    main()
