"""
ברצוננו לחבר קוביות שוקולד לשורה שאורכה x ס"מ. ברשותנו קוביות שוקולד קטנות באורך 1 ס"מ וקוביות שוקולד גדולות באורך 5 ס"מ.

לצורך המשימה כתבו פונקציה שנקראת chocolate_maker המוגדרת כך:

def chocolate_maker(small, big, x):
הפונקציה מקבלת את מספר הקוביות הקטנות (small), את מספר הקוביות הגדולות (big) ואת אורך השורה הרצוי (x). הפונקציה מחזירה אמת אם אפשר ליצור שורה באורך x באמצעות מספר קוביות השוקולד שקיבלה, כולן או חלקן.

הנחיות
אין להשתמש בלולאות.
"""

def chocolate_maker(small, big, x):
    return (small + 5 * big >= x)
