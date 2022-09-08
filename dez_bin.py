def dez_zu_bin(dez_zahl):
    ans = bin(dez_zahl,).replace("0b","")
    print(ans)

def bin_zu_dez(bin_zahl):
    ans =  int(bin_zahl,2)
    print(ans)

bin_zu_dez("1011") 
dez_zu_bin(11)
print("Hello")
