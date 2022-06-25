"""
כתבו תוכנית שקולטת מהמשתמש:

נתיב לקובץ טקסט (מחרוזת)
שם של אחת מן הפעולות: rev, sort או last (מחרוזת)
הקובץ שנתיבו מועבר כארגומנט מכיל שורות של רצפי מילים באותיות אנגליות קטנות שמופרדות ביניהן על-ידי רווח יחיד.

בהתאם לשם הפעולה שנקלטה מן המשתמש התוכנית מבצעת:

sort - התוכנית מדפיסה את כל המילים בקובץ שהועבר כרשימה ממוינת בסדר אלפביתי, ללא כפילויות.
rev - התוכנית מדפיסה את התווים בכל שורה בקובץ בסדר הפוך, כלומר מן הסוף להתחלה.
last - התוכנית קולטת מהמשתמש פרמטר נוסף שהוא מספר שלם (n), ומדפיסה את n השורות האחרונות בקובץ (הניחו שהמספר חיובי וגם קטן או שווה למספר השורות בקובץ).
"""


def get_user_text_file():
    """read a text file from the user
    :return: the string from the text file
    """
    print("Enter a path to a text file: \n")
    path = input()

    path = open(path, "r")

    text_string = path.read()

    path.close()

    return text_string


def sort_text(text_string):
    """sort the list of words alphabetically and remove duplicates
    :param text_string: one long string of words
    :return: none
    """
    sorted_list = text_string.split()
    sorted_list.sort()

    sorted_list = list(dict.fromkeys(sorted_list))  # remove duplicates

    print(sorted_list)


def rev_text(text_string):
    """print each row in reverse order
    :param text_string: one long string of words
    :return: none
    """

    lines_list = text_string.splitlines()

    for line in lines_list:
        for i in range(len(line) - 1, 0, -1):
            print(line[i], end="")
        print()


def last_text(text_string):
    """print the final nth rows of the text
    :param text_string: one long string of words
    :return: none
    """
    print("how many last rows would you like to print from the text: ")
    amount = int(input())

    text_string.strip().split()
    lines_list = text_string.split("\n")

    while amount > 0:
        print(lines_list[-amount])
        amount -= 1


def main():
    text_from_file = get_user_text_file()

    print("enter a command to execute (sort, rev or last): ")
    command = input()

    # print(text_from_file)

    # D:\Users\cijhho123456\Downloads\test.txt

    if command == "sort":
        sort_text(text_from_file)
    elif command == "rev":
        rev_text(text_from_file)
    elif command == "last":
        last_text(text_from_file)
    else:
        print("invalid command. the program will exit.")


if __name__ == "__main__":
    main()
