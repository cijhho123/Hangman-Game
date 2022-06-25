#כתבו תוכנית שממירה בין טמפרטורה במעלות צלזיוס לטמפרטורה במעלות פרנהייט.
#התוכנית קולטת מהמשתמש טמפרטורה: או במעלות צלזיוס, עם סיומת C, או במעלות פרנהייט, עם סיומת F.
#אם הטמפרטורה במעלות צלזיוס, תמיר אותה למעלות פרנהייט, ואם הטמפרטורה במעלות פרנהייט, תמיר אותה למעלות צלזיוס.

print("Insert the temperature you would like to convert:")
temperature = input().lower()               #get the user input
numerical_temperature = float(temperature[0:-1])   #get the numerical value
temperature = temperature[-1]               #mask the numbers


if temperature == "c":
    numerical_temperature = (9 * numerical_temperature + (32 * 5)) / 5
    print(numerical_temperature, "F")
else:
    numerical_temperature = (5 * numerical_temperature - 160) / 9
    print(numerical_temperature, "C")

