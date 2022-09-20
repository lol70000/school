x=0
y=1
out =[]
while x < 23:
    z = 1/2**y
    out.append(z)
    x +=1 
    y +=1
b= [3,5,10,12]
a = 0
c=0
while a<4 :
    c += out[int(b[a])]
    a += 1
print(c)