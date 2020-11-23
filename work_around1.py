STDIN = int(input())
w = len(str(bin(STDIN)).replace('0b',''))

for i in range(1, STDIN+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0o','').rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print (j, o, h, b)