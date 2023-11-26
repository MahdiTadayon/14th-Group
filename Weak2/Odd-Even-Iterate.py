TextString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc"
for i in TextString[::2]:
    print("EVEN :" ,i)
for j in TextString[1::2]:
    print("ODD :" ,j)

print("ReverseText:",TextString[::-1])