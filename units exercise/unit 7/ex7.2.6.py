"""
כתבו תוכנית שקולטת מהמשתמש מחרוזת אחת המייצגת רשימת מוצרים לקניות, מופרדת בפסיקים ללא רווחים.
דוגמה למחרוזת קלט: "Milk,Cottage,Tomatoes".

התוכנית מבקשת מהמשתמש להקיש מספר (ספרה) בטווח אחת עד תשע (אין צורך לבדוק תקינות קלט).
בהתאם למספר שנקלט, מבצעת אחת מן הפעולות הבאות, על פי הפירוט הבא:

הדפסת רשימת המוצרים
הדפסת מספר המוצרים ברשימה
הדפסת התשובה לבדיקה "האם המוצר נמצא ברשימה?" (המשתמש יתבקש להקיש שם מוצר)
הדפסת התשובה לבדיקה "כמה פעמים מופיע מוצר מסוים?" (המשתמש יתבקש להקיש שם מוצר)
מחיקת מוצר מהרשימה (המשתמש יתבקש להקיש שם מוצר, רק מוצר אחד ימחק)
הוספת מוצר לרשימה (המשתמש יתבקש להקיש שם מוצר)
הדפסת כל המוצרים שאינם חוקיים (מוצר אינו חוקי אם אורכו קטן מ-3 או שהוא כולל תווים שאינם אותיות)
הסרת כל הכפילויות הקיימות ברשימה
יציאה
שימו לב, לאחר ביצוע בחירה של המשתמש, המשתמש יחזור לתפריט הראשי עד אשר יבחר ביציאה (יקיש את המספר 9).

הנחיות
העבירו את המוצרים שהתכנית מקבלת לרשימה.
השתמשו בפונקציות נוספות לבחירתכם.
"""


def get_list_from_user():
    """a function that receive a list of groceries from the user and return a list of them
    :return: a list of groceries from the user input
    """
    print("Enter you groceries list:")
    groceries_list_raw = input()

    return groceries_list_raw.split(",")


def menu(user_list):
    """ print the menu and call the selected option
    :return: the selected option
    """

    choice = -1  # python dont have do-while so well...

    while choice != 9 or choice == -1:

        print("""
        Menu:
        1. print the list of items
        2. print the amount of items in the list
        3. print whether or not specific item is on the list
        4. print how many time a specific item is on the list
        5. delete an item from the list (delete only one occurence)
        6. add an item to the list
        7. print all the illigal items on the list (an item is illigal if its name is shorter the 3 characters long or contains non alphabetical characters)
        8. remove all the duplicate items from the list
        9. exit
        
        """)

        choice = int(input())

        match choice:
            case 1:
                print(user_list)
            case 2:
                print("there are ", len(user_list), " items on the list")
            case 3:
                check_for_item_in_list(user_list)
            case 4:
                count_item_occurrences(user_list)
            case 5:
                delete_item_from_list(user_list)
            case 6:
                add_item_to_list(user_list)
            case 7:
                print_illigal_items(user_list)
            case 8:
                user_list = delete_duplicates(user_list)
            case 9:
                return
            case default:
                print("Please choose a valid option!")


def check_for_item_in_list(item_list, test_item="none"):
    """check if an item is on the list
    :param item_list: list of item
    :param test_item: item to check
    :return: True - is in the list      False - not in the list
    """
    if test_item == "none":
        print("Enter item to check:")
        test_item = input()

    if test_item in item_list:
        print(test_item, "is in the list")
        return True
    else:
        print(test_item, "is not in the list")
        return False


def count_item_occurrences(item_list):
    """count how many times a given item appear on the list
    :param item_list: the list
    :return: none
    """
    print("Enter item to count:")
    item = input()

    print(item, "shows up ", item_list.count(item), "in the list")


def delete_item_from_list(item_list):
    """check if an item is on the list, and if so delete one occurence of it
    :param item_list: the list
    :return: none
    """
    print("Enter item to delete:")
    item = input()

    if check_for_item_in_list(item_list, item):
        item_list.remove(item)
        print("item deleted.")
    else:
        print("item wasn't in the list.")


def add_item_to_list(list):
    """add an item to the list
    :param list: the list
    :return: none
    """

    print("Enter item to add to the list: ")
    new_item = input()

    list.append(new_item)


def print_illigal_items(list):
    """print all the items with an illigal name in the list
    :param list: a list of items to check
    :return: none
    """
    all_items_are_valid = True

    for i in list:
        if not name_validation(i):
            print(i)
            all_items_are_valid = False

    if all_items_are_valid:
        print("No items in the list have illigal name.")


def name_validation(name):
    """check if a name is valid. a name is valid if the length is 3 or more and contain only alphabetical characters.
    :param name: name to check
    :return: true - valid       false - invalid
    """
    if not name.isalpha():
        return False
    if len(name) < 3:
        return False
    return True


def delete_duplicates(user_list):
    """remove all the duplicate items from the list
    :param user_list: the list
    :return: the list without duplicates
    """

    return list(set(user_list))




def main():
    groceries_list = get_list_from_user()

    menu(groceries_list)


if __name__ == "__main__":
    main()
