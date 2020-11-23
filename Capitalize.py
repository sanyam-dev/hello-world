def capitalize(name):
    new_name = ""
    for i in range(len(name)):
        if i == 0 and name[i].islower() is True:
            new_name += name[i].upper() 
        elif i != 0:
            new_name += name[i]
    return new_name
    
try:
    string = input("Enter Full Name:")
    string1,string2 = string.split()
except ValueError:
    print("Enter Name and Surname!")
    quit(1)

print(capitalize(string1) + " " +capitalize(string2))




