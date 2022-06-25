"""
צרו מילון עם שם לבחירתכם ואתחלו אותו בהתאם לטבלה הבאה:

Mariah	first_name
Carey	last_name
27.03.1970 (מחרוזת)	birth_date
Sing, Compose, Act (רשימה)	hobbies

כתבו תוכנית שמבצעת את הפעולות הבאות, בהתאם לספרה שהקיש המשתמש:

הדפיסו למסך את שם המשפחה של מריה.
הדפיסו למסך את החודש בו נולדה מריה.
הדפיסו למסך את מספר התחביבים שיש למריה.
הדפיסו למסך את התחביב האחרון ברשימת התחביבים של מריה.
הוסיפו את התחביב "Cooking" לסוף רשימת התחביבים.
הפכו את טיפוס תאריך הלידה לטאפל שכולל 3 מספרים (יום, חודש ושנה - משמאל לימין) והדפיסו אותו.
הוסיפו מפתח חדש בשם age אשר כולל את גילה של מריה והציגו אותו.
הנחיות
בקשו מהמשתמש להכניס קלט (מספר בין 1 ל-7) והניחו שהקלט תקין.
"""
from datetime import date


def menu():
    """print the menu
    :return: none
    """
    print("""
    Menu: ~Mariah Carey Edition~
    1. print the last name
    2. print the month she was born
    3. amount of hobbies
    4. the last hobbit added
    5. add "Cooking" to the hobbies
    6. convert the date of birth to tupple (DD,MM,YYYY)
    7. calculate the current age of Mariah Carey and display it
    """)


def excecute_option(mariah_dict):
    """operate based on the user's selected option
    :param mariah_dict: the info dict
    :return: none
    """
    option = int(input())

    match option:
        case 1:
            print("the last name is: ", mariah_dict["last_name"])
        case 2:
            print("she was born in %sth month" % mariah_dict["birth_date"][4:5])
        case 3:
            print("she has ", len(mariah_dict["hobbies"]), "hobbies.")
        case 4:
            print("the last hobbit added to the dict is ", mariah_dict["hobbies"][-1])
        case 5:
            print("Adding 'Cooking' to the hobbies list")
            mariah_dict["hobbies"].append("Cooking")
            print("the hobbies are now: ", mariah_dict["hobbies"])
        case 6:
            convert_date(mariah_dict)
            print("the date format is converted: ", mariah_dict["birth_date"])
        case 7:
            print("Mariah Carey is %s years old" % calculate_age(mariah_dict))


def convert_date(mariah_dict):
    """convert the birth date from string to tupple
    :param mariah_dict: the info dict
    :return: none
    """
    new_format = mariah_dict["birth_date"]
    new_format = (new_format[0:2], new_format[3:5], new_format[6:10])
    mariah_dict["birth_date"] = new_format


def calculate_age(mariah_dict):
    """calculate mariah's current age (ignoring leap years)
    :param mariah_dict: the info dict
    :return: the curent age
    """
    convert_date(mariah_dict)

    # i am ignoring leap years on the ex.
    today = date.today()
    print(mariah_dict["birth_date"][0])
    age = today.year - int(mariah_dict["birth_date"][2]) - ((today.month, today.day) < (int(mariah_dict["birth_date"][1]), int(mariah_dict["birth_date"][0])))
    return age


def main():
    """ Developer's note:
            so the original question didn't ask for it to be continous menu selection so i did as they asked even tho
            it would make much more sense to do it that way. so it's a bit wacky.
    """
    mariah_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970",
                   "hobbies": ["Sing", "Compose", "Act"]}

    menu()
    excecute_option(mariah_dict)


if __name__ == "__main__":
    main()
