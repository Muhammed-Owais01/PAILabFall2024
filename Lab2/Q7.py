def findAvgTemp(temps):
    total = 0
    for num in temps: total += num
    return total / len(temps)

def highest(temps):
    max = temps[0]
    for num in temps:
        if num > max: max = num
    return max

def lowest(temps):
    min = temps[0]
    for num in temps:
        if num < min: min = num
    return min;

temps = [32,31,34,31,35,34,25,30,25,25,32,27,25,32,29,25,29,27,30,31,32,28,32,35,32,27,25,29,26,34]
temps.sort()

day = int(input("Enter day to remove: "))
if day < 0 or day > 30:
    print("Incorrect day")
else: temps.pop(day - 1)

print("After Removal Count: ", len(temps))
print("Average: ", findAvgTemp(temps))
print("Highest: ", highest(temps))
print("Lowest: ", lowest(temps))