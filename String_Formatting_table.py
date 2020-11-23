import math as m

#Decimal to Binary Conversion in Python
def binary(n):
    quo = n
    bin_str = ""
    while n> 1:
        rem = n%2 
        quo = n/2
        n = m.floor(quo)
        bin_str = str(rem) + bin_str
    bin_str = str(n) + bin_str
    return bin_str

#Decimal to Octal conversion in Python
def octal(n):
    quo = n
    oct_str = ""
    while int(n) > 7:
        rem = n%8
        quo = n/8
        n = m.floor(quo)
        oct_str = str(rem) + oct_str
    oct_str = str(n) + oct_str
    return oct_str

#Decimal to Hexadecimal conversion in Python
def hexadec(n):
    hexa_dec = [[10,"A"],[11,"B"],[12,"C"],[13,"D"],[14,"E"],[15,"F"]]
    quo = n
    hex_str = ""
    while n > 15:
        rem = n%16
        quo = n/16
        n = m.floor(quo)
        if rem < 10:
            hex_str = str(rem) + hex_str 
        elif rem in range(10,16):
            for i in range(len(hexa_dec)):
                if rem == hexa_dec[i][0]:
                    hex_str = hexa_dec[i][1] + hex_str            
    if n in range(1,10):
        hex_str = str(n) + hex_str
    elif n in range(10,16):
        for i in range(len(hexa_dec)):
                if n == hexa_dec[i][0]:
                    hex_str = hexa_dec[i][1] + hex_str
    return hex_str

n = int(input("Enter Number:"))
c = 1
w = len(str(binary(n)))

val_b= "binary".rjust(2*w," ")
num_b = str(binary(n)).rjust(2*w," ")
val_o= "OCTAL".rjust(2*w," ")
num_o = str(octal(n)).rjust(2*w," ")
val_x = "Hexadec".rjust(2*w," ")
num_x = str(hexadec(n)).upper().rjust(2*w," ")
val_n = "Number".rjust(w," ")
num_n = str(n).rjust(w," ")
print(val_n,val_o,val_b,val_x)
print(num_n,num_o,num_b,num_x)
