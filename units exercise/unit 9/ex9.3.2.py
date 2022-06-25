""""
בהמשך לתרגיל הקודם, כתבו פונקציה שנקראת my_mp4_playlist המוגדרת כך:

def my_mp4_playlist(file_path, new_song):
הפונקציה מקבלת כפרמטרים:

נתיב לקובץ (מחרוזת).
בדיוק כמו בתרגיל הקודם, הקובץ מייצג רשימת השמעה של שירים ויש לו פורמט קבוע הבנוי משם השיר, שם המבצע (זמר/להקה) ואורך השיר, המופרדים בנקודה-פסיק (;) ללא רווחים.

דוגמה לקובץ קלט שנקרא songs.txt:
Tudo Bom;Static and Ben El Tavori;5:13;
I Gotta Feeling;The Black Eyed Peas;4:05;
Instrumental;Unknown;4:15;
Paradise;Coldplay;4:23;
Where is the love?;The Black Eyed Peas;4:13;
מחרוזת המייצגת שם של שיר חדש.
פעולת הפונקציה my_mp4_playlist:

הפונקציה כותבת לקובץ את המחרוזת המייצגת שם של שיר חדש (new_song) במקום שם השיר המופיע בשורה השלישית בקובץ (אם הקובץ מכיל פחות משלוש שורות, כתבו לקובץ שורות ריקות כך ששם השיר ייכתב בשורה השלישית).
הפונקציה מדפיסה את תוכן הקובץ לאחר השינוי שבוצע.
"""


def my_mp4_playlist(file_path, new_song):
    songs_file = open(file_path, "r")
    song_list = songs_file.read()
    songs_file.close()

    song_list = song_list.split("\n")

    # check if the list contains at least 3 items
    if len(song_list) < 3:
        while len(song_list) < 3:
            song_list.append("")

    # insert the new song
    song_list[2] = song_list[2].split(";")
    song_list[2][0] = new_song
    song_list[2] = song_list[2][0] + ";" + song_list[2][1] + ";" + song_list[2][2] + ";"

    output = ""
    for song in song_list:
        output += song + "\n"

    songs_file = open(file_path, "w")

    songs_file.write(output)

    return output


def main():
    print(my_mp4_playlist(r"D:\Users\cijhho123456\Downloads\test.txt", "Never Gonna Give You Up"))


if __name__ == "__main__":
    main()
