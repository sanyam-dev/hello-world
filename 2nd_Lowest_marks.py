n = int(input())
if n in range(2,6):
    pass
else: 
    print("ERROR")
marksheet = []

for i in range(n):
    name = input()
    marks = input()
    marksheet.append([name,marks])


marksheet.sort(key = lambda x: float(x[1]))


for i in range(len(marksheet)):
    if marksheet[i][1] == marksheet[1][1]:
        if marksheet[i][0][0] > marksheet[1][0][0]:
            pass
        else :
            s = marksheet[i]
            marksheet.pop(i)
            marksheet.insert(1,s)

print(marksheet[1][0])   
for i in range(2,len(marksheet)):
    if marksheet[i][1] == marksheet[1][1]:
        print(marksheet[i][0])

print(marksheet)
    
   
    


    