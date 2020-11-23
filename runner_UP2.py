import array
import sys
a = array.array('i',[])

n = int(input())
marks = input()
a = [int(i) for i in marks.split()]    
if len(a) != n:
    print("Malicious User!")

for i in range(len(a)):
    if a[i]>=-100 and a[i]<=100:
        pass
    else:
        sys.exit("Value Not In Range!")


def runner_up_score(arr):
    max_score = arr[0]
    target_score = -101
    #break_loop = 0000
    for i in range(len(arr)):
        if max_score < arr[i]:
            target_score = max_score
            max_score =  arr[i]
        elif target_score < a[i] and max_score > a[i]:
            target_score = a[i]
        else:
            pass
        i+=1
    print(target_score)    

runner_up_score(a)
            





