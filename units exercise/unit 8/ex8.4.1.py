"""
הגדירו משתנה קבוע שנקרא HANGMAN_PHOTOS. המשתנה הוא מטיפוס מילון (dict) ועליו להחזיק את שבעת המצבים של האיש התלוי (בהם נתקלתם במשימה המתגלגלת בסוף יחידה 1).
כתבו פונקציה שנקראת print_hangman המוגדרת כך:
def print_hangman(num_of_tries):
הפונקציה מדפיסה את אחד משבעת המצבים של האיש התלוי, בעזרת:
משתנה שנקרא num_of_tries שמייצג את מספר הניסיונות הכושלים של המשתמש עד כה.
המשתנה HANGMAN_PHOTOS שהגדרתם.
"""


def print_hangman(num_of_tries, photo_dict):
    print(photo_dict[num_of_tries])


def create_photo_dict():
    return {1: """
                x-------x
                    """,
            2: """
                x-------x
                |
                |
                |
                |
                |
                    """,
            3: """
                x-------x
                |       |
                |       0
                |
                |
                |
                """,
            4: """
                x-------x
                |       |
                |       0
                |       |
                |
                |
                """,
            5: """
                x-------x
                |       |
                |       0
                |      /|\\
                |
                |
                """,
            6: """
                x-------x
                |       |
                |       0
                |      /|\\
                |      /
                |
                """,
            7: """
                x-------x
                |       |
                |       0
                |      /|\\
                |      / \\
                |
                """}


def main():
    photo_dict = create_photo_dict()
    print("enter a photo to print (1-7)")
    print_hangman(int(input()), photo_dict)


if __name__ == "__main__":
    main()
