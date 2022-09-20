hex_replacement = {"10":"A" ,"11":"B", "12":"C" ,"13":"D","14":"E" ,"15":"F"}
print("Hello")

def cov(dez_num):
    division_result = dez_num
    out_arr= []
    while dez_num > 0 :
        division_result = dez_num // 16
        remaining = dez_num % 16
        if remaining <10 :
            out_arr.append(remaining)
        else:
            out_arr.append(hex_replacement[str(remaining)])
        dez_num = division_result
    out(out_arr)

def out(arr):
    arr.reverse()
    print(arr)

cov(300)
