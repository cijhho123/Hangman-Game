"""
להזכירכם, במשימה המתגלגלת שבסוף היחידה הקודמת כתבתם פונקציה לבדיקות תקינות קלט מהמשתמש. בתרגיל זה תשדרגו את הפונקציה כך שתתייחס בבדיקות גם לאותיות שהשחקן כבר ניחש במשחק.

כתבו שוב את הפונקציה, הפעם קראו לה check_valid_input, והגדירו אותה בצורה הבאה:

def check_valid_input(letter_guessed, old_letters_guessed):
ערכי הקבלה של הפונקציה:
מחרוזת שנקראת letter_guessed. המחרוזת מייצגת את התו שנקלט מן השחקן.
רשימה שנקראת old_letters_guessed. הרשימה מכילה את האותיות שהשחקן ניחש עד כה.
ערכי ההחזרה של הפונקציה
הפונקציה מחזירה ערך בוליאני המייצג את תקינות המחרוזת והאם המשתמש כבר ניחש את התו בעבר.

הפונקציה מחזירה שקר (False, מחרוזת שאינה תקינה) במקרים הבאים:
אם המחרוזת letter_guessed מורכבת משני תווים ומעלה
אם המחרוזת letter_guessed מכילה סימן שאינו אות אנגלית (כמו: &, *)
אם המחרוזת letter_guessed היא תו שכבר נמצא ברשימה old_letters_guessed (כלומר, ניחשו את התו הזה בעבר ולכן לא חוקי לנחש אותו שוב)
הפונקציה מחזירה אמת (True, תו תקין) אם המחרוזת letter_guessed מורכבת מתו אחד בלבד שהוא אות אנגלית (ולא סימן אחר) שאינו נמצא ברשימה old_letters_guessed (כלומר, לא ניחשו את התו הזה בעבר).
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


def main():
    print(check_valid_input('A',['a', 'b', 'c']))
    print(check_valid_input('$',['!', '?', '$']))
    print(check_valid_input('$',['a', 'b', 'c']))
    print(check_valid_input('de',['a', 'b', 'c']))
    print(check_valid_input('a',['a', 'b', 'c']))
    print(check_valid_input('Z',['a', 'b', 'c']))
    print(check_valid_input('z',['a', 'b', 'c']))

if __name__ == "__main__":
    main()
