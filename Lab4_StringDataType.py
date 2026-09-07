myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type" + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("Ano ang iyong pangalan? ")
print(name)

color = input("Ano ang iyong paboritong kulay? ")
animal = input("Ano ang iyong paboritong hayop? ")
print("{}, ang iyong mga gusto ay {} {}!".format(name,color,animal))