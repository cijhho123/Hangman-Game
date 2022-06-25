#כתבו תוכנית שקולטת מהמשתמש מחרוזת לבחירתו.
#התוכנית תדפיס למסך מחרוזת בה כל המופעים של התו הראשון הוחלפו בתו 'e', למעט התו הראשון עצמו.

print("Please enter a string:")
user_input = input()

output = user_input[0] + user_input[1:].replace(user_input[0], "e")

print(output)