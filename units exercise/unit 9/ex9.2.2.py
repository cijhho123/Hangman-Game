"""
כתבו פונקציה שנקראת copy_file_content המוגדרת כך:

def copy_file_content(source, destination):
הפונקציה מקבלת כפרמטרים שתי מחרוזות המייצגות נתיבים של קבצים.
הפונקציה מעתיקה את תוכן הקובץ source אל הקובץ destination.
"""


def copy_file_content(source, destination):
    """Copy the content of source file to destination file
    :param: source, destination: path of files
    :type: string
    """
    source_file = open(source, "r")
    destination_file = open(destination, "w")

    destination_file.write(source_file.read())

    source_file.close()
    destination_file.close()


def main():
    pass


if __name__ == "__main__":
    main()
