"""
כתבו פונקציה בשם last_early המוגדרת כך:

def last_early(my_str):
הפונקציה מקבלת כפרמטר מחרוזת. הפונקציה מחזירה אמת (True) אם התו האחרון שמופיע במחרוזת מופיע גם קודם לכן. אחרת הפונקציה מחזירה שקר (False).
"""

def last_early(my_str):
    print (my_str[-1] in my_str[0:-1])

print("Enter a string: ")
user_input = input()

last_early(user_input)