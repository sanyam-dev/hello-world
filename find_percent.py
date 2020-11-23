global name_list
name_list = []


def name_check(string):
    for i in name_list:
        if string == name_list[i]:
            return True
        else:
            print("NOT FOUND")
    
def marks_entry(string):
    l1 = []
    l1.extend(string.split())
    name_list.append(l1)
    return name_list

def get_marks(name):
    for i in range(len(name_list)):
        if name == name_list[i][0]:
            marks = float((int(name_list[i][1])+int(name_list[i][2])+int(name_list[i][3]))/3)
            print("{0:.2f}".format(marks))
            break
        

#Number of stundents
n = int(input())


#Range Check
if n in range(2,11):
    pass
else:
    print("out of range")

#information of each student
for i in range(n):
    info = input()
    marks_entry(info)

name = input()
get_marks(name)







