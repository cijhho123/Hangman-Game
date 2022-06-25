#התוכנית תקבל כקלט מספר תלת ספרתי (הניחו שהקלט תקין). כל ספרה במספר זה מייצגת את מספר הלבנים שאסף חזיר אחר.
#התוכנית תדפיס את הפלט הבא:
#מספר הלבנים הכולל שאספו החזירונים (כלומר סכום שלוש הספרות)
# הלבנים שיקבל כל חזיר אם יחלקו את מספר הלבנים הכולל שווה בין כולם
#שארית חלוקת הלבנים (כפי שחולקה בסעיף הקודם)
#True אם הסכום מתחלק בין שלושת החזירים ללא שארית, ו-False אחרת. שימו לב, אין להשתמש בהוראת תנאי
#אין להשתמש בלולאות.

print("Enter three digits (each digit for one pig):")

number= int(input())    #read the number from the user and convert it to int
number = number % 10 + (number // 10) % 10 + number // 100   #sum up the digits

print(number)
print((number // 3))
print(number % 3)
print(not (number % 3))