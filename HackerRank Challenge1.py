def is_leap(x):

    if  x > 1899 and x < 100001:
        if int(x) % 4 ==0 :
            if int(x)%100 == 0 :
                if  int(x) %400 == 0:
                    return(bool(1))   
                else :
                    return(bool(0))         
            else :
             return(bool(1))
        else :
          return(bool(0))
    else:
        print("OUT OF DEFINED RANGE!")
       



year = int(input())
print(is_leap(year))