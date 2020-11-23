def swap_case(string):   
    str_element = []
    for i in range(len(string)):
        str_element.append(string[i])
        if str_element[i].isupper() is True:
            str_element[i] = str(str_element[i].lower())
        elif str_element[i].islower() is True:
            str_element[i] = str(str_element[i].upper())    
    s = "".join(str_element)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)