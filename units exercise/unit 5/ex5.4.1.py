"""
בתרגיל זה תתרגלו קונבנציות בכתיבת תוכניות ותיעוד לפונקציות באמצעות פונקציה פשוטה שתכתבו בעצמכם.

לצורך המשימה כתבו פונקציה בשם func המוגדרת כך:

def func(num1, num2):
    <return a value>
החליטו מה תהיה פעולת הפונקציה וכתבו אותה בהתאם. בהתאמה להחלטתכם עבור פעולת הפונקציה, תעדו אותה כראוי, עם התייחסות לפרמטרים ולערך ההחזרה.

הנחיות
התוכנית שלכם תכלול את הפונקציה func ואת התיעוד שלה, וכן קריאה לפונקציה help להצגת התיעוד של הפונקציה func.
הקפידו לכתוב את התיעוד בהתאמה למבנה שמוצג בפרק בנושא "תיעוד פונקציה".
הקפידו על כתיבת הקוד (בתרגיל זה וגם בתרגילי כתיבת הקוד מעתה והלאה) במבנה הבא:
def main():
    # Call the function func

if __name__ == "__main__":
    main()
במידת הצורך חזרו על הנושא בפרק שעוסק בפונקציה main.
"""


def add(num1, num2):
    """A function that add two numbers.
    :param num1: the first number
    :param num2: the second number
    :return: the sum of the two parameters
    """
    return num1 + num2


def main():
    print(add(1, 5))


if __name__ == "__main__":
    main()