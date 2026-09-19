temp=int(input("enter the temp "))
the_charger_is_plugged_in=input("the charger is plugged in")
if temp>=90 and the_charger_is_plugged_in=="yes":
    print("Warning: Critical temperature! Open ThrottleStop to reduce voltage.")
elif temp>=80 and the_charger_is_plugged_in=="yes":
    print("Temperature is normal under load.")
elif temp<75 :
    print("deviice is in safe mode")
elif temp<60:
    print("device is wonderful")


