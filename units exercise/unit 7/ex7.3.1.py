"""
תבו פונקציה שנקראת show_hidden_word המוגדרת כך:

def show_hidden_word(secret_word, old_letters_guessed):
ערכי הקבלה של הפונקציה
מחרוזת שנקראת secret_word. המחרוזת מייצגת את המילה הסודית שהשחקן צריך לנחש.
רשימה שנקראת old_letters_guessed. הרשימה מכילה את האותיות שהשחקן ניחש עד כה.
ערכי ההחזרה של הפונקציה
הפונקציה מחזירה מחרוזת אשר מורכבת מאותיות ומקווים תחתונים. המחרוזת מציגה את האותיות מתוך הרשימה old_letters_guessed שנמצאות במחרוזת secret_word במיקומן המתאים, ואת שאר האותיות במחרוזת (אותן השחקן טרם ניחש) כקווים תחתונים.
"""


def show_hidden_word(secret_word, old_letters_guessed):
    """print the current state of the guesses word
    :param secret_word: the word
    :param old_letters_guessed: list of used letters
    :return: the current state of the guessing as a string
    """
    output = ""

    for i in secret_word:
        if i in old_letters_guessed:
            output += i + " "
        else:
            output += "_ "

    output = output[0:-1]

    return output


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()
