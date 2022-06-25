"""
בתרגיל הזה תפעלו בהתאמה לתו החדש שהשחקן ניחש: או שתוסיפו אותו לרשימת הניחושים, או שתדפיסו הודעה אם אי אפשר להוסיפו.

כתבו פונקציה שנקראת try_update_letter_guessed המוגדרת כך:

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
ערכי הקבלה של הפונקציה
מחרוזת שנקראת letter_guessed. המחרוזת מייצגת את התו שנקלט מהשחקן.
רשימה שנקראת old_letters_guessed. הרשימה מכילה את האותיות שהשחקן ניחש עד כה.
פעולת הפונקציה
אם התו תקין (כלומר אות אנגלית אחת) ולא ניחשו אותו בעבר, הפונקציה תוסיף את התו letter_guessed לרשימה old_letters_guessed. לאחר מכן תחזיר ערך אמת (True) שמציין שההוספה התבצעה בהצלחה.
אם התו אינו תקין (כלומר אינו אות אנגלית אחת) או שהוא נמצא כבר ברשימת הניחושים, הפונקציה תדפיס את התו X (האות הגדולה X) ומתחתיו את הרשימה old_letters_guessed כמחרוזת של אותיות קטנות שממוינות מהקטן לגדול ומופרדות זו מזו בחצים (חץ מורכב מהסימנים: <-, ראו פלט לדוגמה). הדפסת האיברים נועדה להזכיר לשחקן אילו תווים הוא ניחש כבר. בסיום, הפונקציה תחזיר ערך שקר (False) שמשמעותו שאין אפשרות להוסיף את התו לרשימת התווים שניחשו כבר.
הנחיה
היעזרו בפונקציה check_valid_input שמימשתם בתרגיל הקודם.
"""


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check for a proper user input
    :param letter_guessed: the letter the user have guesses
    :param old_letters_guessed: already used letters
    :return: True - valid input     False - invalid input
    """
    letter_guessed = letter_guessed.lower()

    if len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """a function that receive a letter guesses by the user and a string of already used letters and try to assign the
    newly guessed letter to the list if it is valid.
    :param letter_guessed: the letter the used guesses
    :param old_letters_guessed: list of used letters
    :return: True - succeeded        False - failed
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        used_letters = format_list(old_letters_guessed)
        print(used_letters)
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def format_list(my_list):
    """a function that recive a list of strings and return a string of all the concatenated strings separated by an
    arrow in a sorted alphabetical order.

    :param my_list: list of string
    :return: the concatenated string
    """
    my_list.sort()
    return ' -> '.join(my_list[:])


def main():
    cool_list = ['a', 'p', 'c', 'f']
    print(cool_list)
    print(format_list(cool_list))


if __name__ == "__main__":
    main()
