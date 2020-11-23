#Exercise on Data types in Python
def TestData(Candid_Name):
    Candid_Name = []
    
    #Candid_Name.append(str(Candid_Name))
    counter = 1
    while counter < 4:
        m = int(input(" Enter The Marks :"))
        Candid_Name.append(m) 
        counter = counter + 1
    Avg_Marks = (Candid_Name[0] + Candid_Name[1] + Candid_Name[2])/3
    return Candid_Name
    return Avg_Marks
    
n  = int(input("Number of Candidates : "))

#counter variable
j = 0
while j<n:
    name = str(input("Enter Candidate Name : "))
    TestData(name)
    j = j + 1

print(TestData(name))