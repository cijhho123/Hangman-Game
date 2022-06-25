"""
כתבו פונקציה בשם distance המוגדרת כך:

def distance(num1, num2, num3):
הפונקציה מקבלת שלושה מספרים שלמים: num1, num2, num3.

הפונקציה מחזירה אמת (True) אם מתקיימים שני התנאים:

אחד מהמספרים num2 או num3 "קרוב" ל-num1. "קרוב" = מרחק אבסולוטי 1.
אחד מהמספרים num2 או num3 "רחוק" משני המספרים האחרים. "רחוק" = מרחק אבסולוטי 2 ומעלה.
"""

def distance(num1, num2, num3):
    #contition #1
    if abs(num1 - num2) != 1 and abs(num1 - num3) != 1:
        return False

    #condition #2
    if (abs(num2 - num1) > 1 and abs(num2 - num3) > 1) or (abs(num3 - num1) > 1 and abs(num3 - num2) > 1):
        return True
    else:
        return False


