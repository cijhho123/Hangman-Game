"""
 זוכרים את המשימה המתגלגלת בסוף היחידה הקודמת, בה קלטנו מהשחקן תו לניחוש? האם תהיתם מה קורה אם השחקן הקליד בטעות תו שאיננו אות אנגלית? או יותר מתו אחד?
כאשר אנו מבקשים קלט מן המשתמש, עלינו להניח שהקלט לא בהכרח יהיה תקין ולכן באחריותנו לבצע עליו בדיקות תקינות.

בתרגיל זה עליכם לקלוט תו מהמשתמש (השחקן). בהתאם לתו שנקלט הדפיסו הודעה למסך בנוגע לתקינות שלו, על פי הדרישות הבאות:

עבור תו שאינו תקין:
אם השחקן הזין מחרוזת אותיות הכוללת יותר מתו אחד, הדפיסו למסך את המחרוזת "E1".
אם השחקן הזין תו שאינו אות אנגלית (לדוגמה סימן כמו: &, *), הדפיסו למסך את המחרוזת "E2".
אם השחקן הזין מחרוזת אותיות הכוללת יותר מתו אחד וגם מכילה תווים שאינם אותיות באנגלית, הדפיסו למסך את המחרוזת "E3".
עבור תו תקין:
אם התו שנקלט הוא תו אחד וגם אות אנגלית (ולא סימן אחר) הדפיסו אותו למסך כאות קטנה.
"""
print("Guess a letter:")
letter = input().lower()

if len(letter) > 1:
    if letter.isalpha():
        print("E1")
    else :
        print("E3")
elif not letter.isalpha():
    print("E2")
else:
    print(letter)