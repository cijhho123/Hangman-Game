"""
כתבו פונקציה בשם are_lists_equal המוגדרת כך:

def are_lists_equal(list1, list2):
הפונקציה מקבלת שתי רשימות המכילות איברים מהטיפוסים int ו-float בלבד. הפונקציה מחזירה אמת אם שתי הרשימות מכילות בדיוק את אותם האיברים (גם אם בסדר שונה), אחרת, הפונקציה מחזירה שקר.

הנחיות
אין להשתמש בלולאות.
"""

def are_lists_equal(list1, list2):
    """check if two lists contain the same numbers regardless of order
    :param list1: first list
    :param list2: second list
    :return: True - same numbers in both lists       False - not the same numbers
    """

    list1.sort()
    list2.sort()

    return list1 == list2




def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]

    print(are_lists_equal(list1, list3))

if __name__ == "__main__":
    main()