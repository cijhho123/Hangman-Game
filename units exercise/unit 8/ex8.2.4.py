"""
כתבו פונקציה שנקראת sort_anagrams המוגדרת כך:

def sort_anagrams(list_of_strings):
הפונקציה מקבלת כפרמטר רשימת מחרוזות, כך שכל מחרוזת היא מילה אחת (ללא רווחים).
הפונקציה מחזירה רשימה של אותן מחרוזות שהועברו, אך באופן הבא: הרשימה מחולקת לרשימות כך שכל רשימה "פנימית" מורכבת ממילים שהן אנגרמות אחת של השנייה (אנגרמה: מילה המורכבת משֹיכול אותיות של מילה אחרת, כלומר אותן אותיות אך בסדר שונה).

הנחיות
דאגו שהמחרוזות והרשימות יהיו מסודרות לפי סדר הופעתן של המחרוזות ברשימה המקורית.
"""


def sort_anagrams(list_of_strings):
    """recive a list of strings and return a list of lists of anagrams
    :param list_of_strings: list of strings
    :return: list of lists by anagrams
    """
    anagram_list = []

    for i in list_of_strings:
        match_found = False

        for a in anagram_list:
            if sorted(i) == sorted(a[0]):
                a.append(i)
                match_found = True

        if not match_found:
            anagram_list.append([i,])

    return anagram_list


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

    print(sort_anagrams(list_of_words))


if __name__ == "__main__":
    main()
