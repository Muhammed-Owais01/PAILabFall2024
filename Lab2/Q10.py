def build_message(**info):
    return f'Name: {info["Name"]}, Age: {info["Age"]}, City: {info["City"]}'

print(build_message(Name = "Owais", Age = 21, City = "Karachi"))