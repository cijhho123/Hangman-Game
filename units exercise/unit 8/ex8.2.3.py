"""
כתבו פונקציה שנקראת mult_tuple המוגדרת כך:

def mult_tuple(tuple1, tuple2):
הפונקציה מקבלת כפרמטרים שני איברים מהטיפוס טאפל.
הפונקציה מחזירה טאפל המכיל את כל הזוגות שאפשר ליצור מאיברי הטאפלים שהועברו כארגומנטים.

הנחיות
כדי לייצג את כל הזוגות, החזירו גם זוגות עם איברים בסדר הפוך. לדוגמה: הזוג (1 ,4) יוחזר בנוסף לזוג (4 ,1).
"""


def mult_tuple(tuple1, tuple2):
    merged_tuple = []  # currently working with list because tuple is immutable
    for i in tuple1:
        for j in tuple2:
            merged_tuple.append((i, j))
            merged_tuple.append((j, i))

    return tuple(merged_tuple)


def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == "__main__":
    main()
