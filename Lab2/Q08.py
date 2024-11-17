conversionRates = [  
    [1, 1.11, 309.54, 93.25, 160.80], # eur to
    [0.90, 1, 278.62, 83.94, 144.74], # usd to
    [0.0032, 0.0036, 1, 0.30, 0.52], # pkr to
    [0.011, 0.012, 3.32, 1, 1.72], # inr to
    [0.0062, 0.0069, 1.93, 0.58, 1] # yen to
]

def convert(amount, convertFrom, convertTo):
    return amount * conversionRates[convertFrom][convertTo]

amount = float(input("Enter amount: "))
print("1- EUR", "2- USD", "3- PKR", "4- INR", "5- YEN", sep="\n")
convertFrom = int(input("Convert From: "))
convertTo = int(input("Convert To: "))

print(convert(amount, convertFrom - 1, convertTo - 1))