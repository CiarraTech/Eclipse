RateOfSpeed = 0.00
SpeedLimit = 55.00
FineAmount = 0.00
FineMessage = "There is no message defined."

#Determine the rate of speed
RateOfSpeed = input("Please input the rate of speed in miles per hour:   ")

#No fine if under 55MPH
if (RateOfSpeed <= 55):
    FineMessage = "There is no fine."
elif (RateOfSpeed <= 75):
    FineAmount = ((RateOfSpeed - SpeedLimit)* 5.00) + 50.00
    FineMessage = "The fine is " + str(FineAmount)
else:
    FineAmount = ((RateOfSpeed - SpeedLimit)* 5.00) + 50.00 + 200
    FineMessage = "The fine is " + str(FineAmount)
#YOLO  I'm programming
print FineMessage
