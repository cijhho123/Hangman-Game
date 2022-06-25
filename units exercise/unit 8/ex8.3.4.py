"""
כתבו פונקציה שנקראת inverse_dict המוגדרת כך:

def inverse_dict(my_dict):
הפונקציה מקבלת כפרמטר מילון.
הפונקציה מחזירה מילון חדש עם מיפוי "הפוך": כל מפתח במילון שמועבר הוא ערך במילון שמוחזר וכל ערך במילון שמועבר הוא מפתח במילון שמוחזר.

הנחיות
ההיפוך בין מפתחות לבין ערכים עלול ליצור מפתחות שמופיעים יותר מפעם אחת. לכן, יצגו את הערכים במילון שמוחזר כרשימה, שעשויה להכיל ערך אחד או יותר.
הרשימות המוחזרות צריכות להיות ממוינות (אפשר להניח שהערכים במילון הם מאותו הטיפוס).
"""


def inverse_dict(my_dict):
    inv_dict = {}

    for i in my_dict.items():
        if i[1] in inv_dict:
            inv_dict[i[1]].append(i[0])
        else:
            inv_dict[i[1]] = [i[0], ]

    # sort the lists
    for i in inv_dict.items():
        i[1].sort()

    return inv_dict


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == "__main__":
    main()
