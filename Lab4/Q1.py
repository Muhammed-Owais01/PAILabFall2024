a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]

combList = []
for i in range(0, len(a)):
    combList.append(a[i] + b[i])
print(combList)


# SINGLE LINE
print([(a[i] + b[i]) for i in range(0, len(a))])
