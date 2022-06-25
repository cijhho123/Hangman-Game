"""
הגיע הזמן לבדוק אם השחקן כבר ניצח, לא?
בתרגיל זה תכתבו פונקציה שבודקת האם השחקן הצליח לנחש את המילה הסודית ובכך ניצח במשחק!

כתבו פונקציה שנקראת check_win המוגדרת כך:

def check_win(secret_word, old_letters_guessed):
ערכי הקבלה של הפונקציה
מחרוזת שנקראת secret_word. המחרוזת מייצגת את המילה הסודית שהשחקן צריך לנחש.
רשימה שנקראת old_letters_guessed. הרשימה מכילה את האותיות שהשחקן ניחש עד כה.
ערכי ההחזרה של הפונקציה
הפונקציה מחזירה אמת (True) אם כל האותיות שמרכיבות את המילה הסודית נכללות ברשימת האותיות שהמשתמש ניחש. אחרת, הפונקציה מחזירה שקר (False).
"""

def check_win(secret_word, old_letters_guessed):
    """check if the secred word is guessed
    :param secret_word: the word the user is trying to guess
    :param old_letters_guessed: list of guesses letters
    :return: true if it guesses, false otherwise
    """
    for i in secret_word:
        if i not in old_letters_guessed:
            return False

    return True

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()
