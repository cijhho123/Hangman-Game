""""
במשימה זו תבחרו עבור השחקן מילה שתהיה המילה הסודית לניחוש, מתוך קובץ טקסט המכיל רשימת מילים מופרדות ברווחים.

כתבו פונקציה שנקראת choose_word המוגדרת כך:

def choose_word(file_path, index):
הפונקציה מקבלת כפרמטרים:

מחרוזת (file_path) המייצגת נתיב לקובץ הטקסט.
מספר שלם (index) המייצג מיקום של מילה מסוימת בקובץ.
הפונקציה מחזירה טאפל המורכב משני איברים בסדר הבא:

מספר המילים השונות בקובץ, כלומר לא כולל מילים שחוזרות על עצמן.
מילה במיקום שהתקבל כארגומנט לפונקציה (index), שתשמש בתור המילה הסודית לניחוש.
הנחיות
התייחסו למיקומים שהשחקן מכניס כמתחילים מ-1 (ולא מאפס).
אם המיקום (index) גדול ממספר המילים בקובץ, הפונקציה ממשיכה לספור מיקומים בצורה מעגלית (כלומר, חוזרת למיקום הראשון ברשימת המילים המקורית בקובץ וחוזר חלילה).
"""


def choose_word(file_path, index):
    words_file = open(file_path, "r")
    word_list = words_file.read()
    words_file.close()

    word_list = word_list.split(" ")

    print(word_list)

    info_tuple = (len(set(word_list)),word_list[len(word_list) % index])
    return info_tuple


def main():
    print(choose_word(r"D:\Users\cijhho123456\Downloads\test.txt", 3))


if __name__ == "__main__":
    main()
