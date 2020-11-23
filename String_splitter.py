def string_split(string):
    element = []
    element.extend(string.split())
    return element

str1  = input()
l1 = string_split(str1)
print(l1[0][0])




