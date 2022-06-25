"""
נתונה התוכנית:

data = ("self", "py", 1.543)
format_string = "Hello"

print(format_string % data)
עדכנו את המשתנה format_string כך שיודפס:

Hello self.py learner, you have only 1.5 units left before you master the course!
הנחיות
השתמשו במשתנה הנתון data.
שימו לב שמודפסת רק ספרה אחת אחרי הנקודה (כלומר המספר 1.5).
"""
def main():
    data = ("self", "py", 1.543)
    format_string = "Hello {}.{} learner, you have only {:.2} units left before you master the course!"

    print(format_string.format(*data))


if __name__ == "__main__":
    main()
