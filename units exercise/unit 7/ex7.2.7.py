"""
כתבו פונקציה שנקראת arrow המוגדרת כך:

def arrow(my_char, max_length):
הפונקציה מקבלת שני פרמטרים: הראשון תו בודד, השני הוא גודל מקסימלי.
הפונקציה מחזירה מחרוזת המייצגת מבנה של "חץ" (ראו דוגמה), הבנוי מתו הקלט, כאשר מרכז החץ (השורה הארוכה ביותר) הוא באורך הגודל שמועבר כפרמטר.

דוגמה להרצה של הפונקציה arrow
print(arrow('*', 5))
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
בדוגמה זו מעבירים את התו כוכבית * ואת הגודל המירבי 5. כלומר, השורה האמצעית היא באורך 5.
"""


def arrow(my_char, max_length):
    output = ""

    for i in list(range(1,max_length)):
        output +=  (my_char * i) + "\n"

    for i in list(range(max_length, 0, -1)):
        output += (my_char * i) + "\n"

    output = output[0:-1]
    return output

def main():

    print(arrow("*", 5))


if __name__ == "__main__":
    main()
