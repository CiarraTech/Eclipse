#Get TempF from user
TempF = input("Please enter the temperature in degrees F:")
print str(TempF) + " Degrees Fahrenheit"

#Use the standard formula to convert TempF => TempC
TempC = (TempF - 32)/1.8
print "Is equal to " + str(TempC) + " degrees Celsius."
