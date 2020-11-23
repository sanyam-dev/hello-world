s = input()
if len(s) in range(3,10000):
    p =''.join(sorted(s))
else:
    print("error!")


l1 = []
if len(l1) == 0:
    l1.append([p[0],1])
for i in range(1,len(s)):
    cdwd = 0 
    
    for j in range(len(l1)):
        if p[i] == l1[j][0]:
            l1[j][1] += 1
            cdwd = 0
            break
        elif p[i] != l1[j][0]:
            cdwd = 1
    if cdwd == 1:
        l1.append([p[i],1])
        cdwd = 0


l1.sort(key = lambda x: x[1],reverse=True)


for i in range(3):
    print(l1[i][0], l1[i][1])

                


        
        
