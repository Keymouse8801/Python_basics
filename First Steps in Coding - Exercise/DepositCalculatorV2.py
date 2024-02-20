depositAmmount = int(input())
depositDurotation = int(input())
depositInterest = float(input()) / 100 #Има деление, защото има проценти!

finalAmmount = depositAmmount + depositDurotation*((depositAmmount * depositInterest) / 12)
print(finalAmmount)