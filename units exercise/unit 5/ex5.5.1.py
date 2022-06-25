"""
במשימה שבסוף היחידה הקודמת טיפלתם בצורה יסודית במקרים שבהם השחקן מקליד קלט שאינו תקין. כיוון שהמשחק "איש תלוי" כולל ניחושים רבים עולה השאלה: האם נעתיק את כל שורות הקוד הללו שוב ושוב עבור כל ניחוש? כמובן שלא.

לכן נאגד חלק מהלוגיקה מן המשימה הקודמת בתור פונקציה שנקראת is_valid_input. הפונקציה מוגדרת כך:

def is_valid_input(letter_guessed):
ממשו את הפונקציה is_valid_input. הפונקציה מקבלת כפרמטר את המחרוזת letter_guessed, שמייצגת את התו שנקלט, ומחזירה ערך בוליאני המייצג אם התו תקין או לא.

הפונקציה מחזירה שקר (False, מחרוזת שאינה תקינה) במקרים הבאים:
אם המחרוזת letter_guessed מורכבת משני תווים ומעלה
אם המחרוזת letter_guessed מכילה סימן שאינו אות אנגלית (כמו: &, *)
הפונקציה מחזירה אמת (True, תו תקין) אם המחרוזת letter_guessed מורכבת מתו אחד בלבד שהוא אות אנגלית (ולא סימן אחר).

הנחיות
הקפידו על פלט מדויק.
היעזרו בתוכנית שכתבתם במשימה שבסוף היחידה הקודמת.
"""


def is_valid_input(letter_guessed):
    """Check for a proper user input
    :param letter_guessed: the input from the user
    :return: true - valid input         false -invalid input
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def main():
    print("Guess a letter:")
    letter = input().lower()

    print(is_valid_input(letter))


if __name__ == "__main__":
    main()
