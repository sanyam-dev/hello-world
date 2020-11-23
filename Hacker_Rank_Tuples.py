
n = int(input())
str_len = 2*n - 1

int_str = input()

t= tuple(map(int, int_str.split()))
if int(len(t)) == n:
    pass
else:
    print("Error")
    SystemExit
print(hash(t))



    