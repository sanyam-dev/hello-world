import array

def print_arr(arr,n):
    for i in range(0,n):
        print(arr[i], end = " ")

def runner_up(arr):
    count = len(arr)
    max1 = -101
    break_loop = 1904
    #break_loop code is changed by a conditional statement which further breaks the loop
  
    #Finding the max marks
    for i in range(0,count):

        if max1 < arr[i]:
            max1 = arr[i]
    # initial run_up score be less than the whole range     
    run_up = -101
    for i in range(1, 101):
        run_up = max1 - i
        i += 1
        #Checking if the nearest lowest value is present in the array
        for  j in range(0,n):
            if run_up == a[j]: 
                break_loop = 1234
                break
    
        if break_loop == 1234:
            break  
    print(run_up)
    
#Total Students 
try:
    n = int(input("Enter Total Students: "))
except n < 2 or n > 10:
    print("Try Again")
    n = int(input("Enter Total Students: "))

a = array.array('i',[])
i = 0
while  i < n:
   
    try:
        mrks = int(input("Enter Marks: "))
    except mrks in range(-100,101):
        print("enter marks in range")
    
    i += 1
    a.append(mrks)
#Finding Max Marks
max_mrks = -101
for i in range(0,n):
    if max_mrks < a[i]:
        max_mrks = a[i]
#The function written up there was first executed here

break_loop = 10001
run_up = 0
for i in range(1, 101):
    run_up = max_mrks - i
    i += 1
    for  j in range(0,n):
        if run_up == a[j]:
            print(run_up)   
            break_loop = 1234
            break
    
    if break_loop == 1234:
        break  

print("*** ---- *** ---- ***")

runner_up(a)
    


   

    








            


