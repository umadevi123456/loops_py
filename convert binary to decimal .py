# n=int(input("binary number:"))
# value=0
# for i in range(len(n)):
#     digit=n.pop()
#     if digit=="1":
#         value =value+pow(2,i)
# print("the decimal value of the number is",value)


a=int(input("binary number"))
b=0
i=1
while a!=0:
    r=a%10
    b=b+(r*i)
    i=i*2
    a=int(a/10)
print(b)






