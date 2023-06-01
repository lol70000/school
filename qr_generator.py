import qrcode
data = input("What is your data")
img = qrcode.make(data)
name = input("what ist the Name of your qrcode")
img.save(str(name)+".png")