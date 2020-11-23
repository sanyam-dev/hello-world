global expense
expense = []
Months = ["January" ,"February", "March" ,"April", "May","June", "July", "August","September", "October", "Novemeber", "December"]
response = ["Y","Yes","YES","yes","y"]
n  = int(input("No. of Months:"))
if n in range(13):
    pass
else:
    print("ERROR MESSAGE!")

def add_data(month,exp_data):
    expense.append([month,exp_data])
    return(expense)

def track_input(num1):
    for i in range(len(expense)):
        if num1 == expense[i][1]:
            print("Expense Found for Month:",expense[i][0])
        else:
            int1 =1903
    if int1 == 1903:
        print("Expense NOT Found")

def Refund_data(num1,month1):
    for i in range(len(expense)):
        if month1 == expense[i][0]:
            expense[i][1] = expense[i][1] - num1
            return(expense)
        else:
            print("NO ENTRY FOUND!")


def exp_input(n):
    for i in range(n):
        expense.append([])
        for j in [0,1]:
            if j == 0:
                expense[i].append(Months[i])
                print("Month:",expense[i][0])
            else:
                expense[i].append(input("Expense:"))

exp_input(n)

def compare(month1,month2):
    exp1 = 0
    exp2 = 0
    for i in range(len(expense)):
        if month1 == expense[i][0]:
            exp1 = int(expense[i][1])
        if month2 == expense[i][0]:
            exp2 = int(expense[i][1])
    extra = exp1 - exp2
    print("You Spent",extra,"extra in",month2,"as compared to",month1)

if input("Do You wanna compare expenses?") in response:
    month1 = input("Month1 =")
    month2 = input("Month2 =")
    compare(month1,month2)
else:
    pass

if input("Do You Want to Append The Expense List ?") in response:
    month = input("Month:")
    exp_data = input("Expense:")
    add_data(month,exp_data)
else:
    pass

if input("Do You Want to Track Expense") in response:
    data = input("Enter tracking data:")
    track_input(data)

if input("Did You Get Any Refund?") in response:
    Refund_input = input("Refund Amount:")
    Refund_month = input("Month:")
    Refund_data(Refund_month,Refund_input)

if n >= 5 and input("Do You Want to know your quareterly expense ") in response:
    sum = 0
    for i in range(len(expense)):
        sum  = sum + int(expense[i][1])
    print("Rs.",sum,"is your quarterly expense.")
else:
    pass
