""""
כתבו פונקציה שנקראת my_mp3_playlist המוגדרת כך:

def my_mp3_playlist(file_path):
הפונקציה מקבלת כפרמטר נתיב לקובץ (מחרוזת).
הקובץ מייצג רשימת השמעה של שירים ויש לו פורמט קבוע הבנוי משם השיר, שם המבצע (זמר/להקה) ואורך השיר, המופרדים בנקודה-פסיק (;) ללא רווחים.

דוגמה לקובץ קלט שנקרא songs.txt:

Tudo Bom;Static and Ben El Tavori;5:13;
I Gotta Feeling;The Black Eyed Peas;4:05;
Instrumental;Unknown;4:15;
Paradise;Coldplay;4:23;
Where is the love?;The Black Eyed Peas;4:13;
הפונקציה מחזירה טאפל שבו:

האיבר הראשון הוא מחרוזת המייצגת את שם השיר הארוך ביותר בקובץ (הכוונה היא לשיר הארוך ביותר, הניחו שכל האורכים שונים).
האיבר השני הוא מספר המייצג את מספר השירים שהקובץ מכיל.
האיבר השלישי הוא מחרוזת המייצגת את שם המבצע שמופיע בקובץ מספר הפעמים הגדול ביותר (הניחו שיש רק אחד כזה).
"""


def my_mp3_playlist(file_path):
    songs_file = open(file_path, "r")
    song_list = songs_file.read()
    songs_file.close()

    song_list = song_list.split(";")

    info_tuple = ()

    # look for the longest name in the file
    max_length = 0
    song_of_max_length = 0

    for x in range(2, len(song_list), 3):
        current_time = int(song_list[x].split(":")[0]) * 60 + int(song_list[x].split(":")[1])

        if current_time > max_length:
            max_length = current_time
            song_of_max_length = song_list[x - 2]

    info_tuple = info_tuple + (song_of_max_length,)

    # the amount of songs
    amount_of_songs = (len(song_list) - 1) / 3
    info_tuple = info_tuple + (int(amount_of_songs),)

    # the most frequent performer
    performer_counter = {}
    for x in range(1, len(song_list), 3):
        current_artist = song_list[x]

        if current_artist in performer_counter:
            performer_counter[current_artist] += 1
        else:
            performer_counter[current_artist] = 1

    max_occurences = 0
    max_name = ""

    for key, value in performer_counter.items():
        if value > max_occurences:
            max_occurences = value
            max_name = key

    info_tuple = info_tuple + (max_name,)

    return info_tuple


def main():
    print(my_mp3_playlist(r"D:\Users\cijhho123456\Downloads\test.txt"))


if __name__ == "__main__":
    main()
