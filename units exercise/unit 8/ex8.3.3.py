"""
כתבו פונקציה שנקראת count_chars המוגדרת כך:

def count_chars(my_str):
הפונקציה מקבלת מחרוזת כפרמטר.
הפונקציה מחזירה מילון, כך שכל איבר בו הוא צמד שמורכב ממפתח: תו מן המחרוזת שהועברה (לא כולל רווחים), ומערך: מספר הפעמים שהתו מופיע במחרוזת.
"""


def count_chars(my_str):
    counter = {}

    for i in my_str:
        # skip over whitespaces
        if i.isspace():
            continue

        if i in counter:
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1

    return counter


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))


if __name__ == "__main__":
    main()
