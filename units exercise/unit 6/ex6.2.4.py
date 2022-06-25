"""
כתבו פונקציה בשם extend_list_x המוגדרת כך:
def extend_list_x(list_x, list_y):
הפונקציה מקבלת שתי רשימות list_y, list_x. הפונקציה מרחיבה את list_x (משנה אותה) כך שתכיל בתחילתה גם את list_y, ומחזירה את list_x.

דוגמה להרצת הפונקציה extend_list_x
>>> x = [4, 5, 6]
>>> y = [1, 2, 3]
>>> extend_list_x(x, y)
[1, 2, 3, 4, 5, 6]
הנחיות
אין להשתמש באופרטור '+'.
אין להשתמש במתודה extend.

"""

def extend_list_x(list_x, list_y):
    temp_list = list_y.copy()
    list_x = temp_list.__add__(list_x)


    return list_x


def main():
    x = [4, 5, 6]
    y = [1, 2, 3]

    x = extend_list_x(x,y)
    print(x)

if __name__ == "__main__":
    main()