s = input()
def List_check(l):
    if len(l) == 0:
        print("False")
    else:
        print("True")
alnum = []
alpha = []
digit = []
lower = []
upper = []
for i in range(len(s)):
    if str.isalnum(s[i]) is True:
        alnum.append(s[i])
    else:
        pass

for i in range(len(s)):
    if str.isalpha(s[i]) is True:
        alpha.append(s[i])
    else:
        pass

for i in range(len(s)):
    if str.isdigit(s[i]) is True:
        digit.append(s[i])
    else:
        pass

for i in range(len(s)):
    if str.islower(s[i]) is True:
        lower.append(s[i])
    
for i in range(len(s)):
    if str.isupper(s[i]) is True:
        upper.append(s[i])

List_check(alnum)
List_check(alpha)
List_check(digit)
List_check(lower)
List_check(upper)

