#כתבו תוכנית שקולטת מהמשתמש מחרוזת לבחירתו.
#התוכנית מדפיסה את המחרוזת כאשר האותיות בחצי הראשון של המחרוזת הן אותיות קטנות, והאותיות בחצי השני של המחרוזת הן אותיות גדולות.
#אם אורך המחרוזת אי זוגי, החצי הראשון יהיה קטן באחת מהחצי השני.

print("Please enter a string:")
user_input = input()

output = user_input[:len(user_input)//2].lower() + user_input[len(user_input)//2:].upper()

print(output)