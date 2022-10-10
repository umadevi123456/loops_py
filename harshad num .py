# n=(input("enter number"))
# i=0
# sum=0
# while i<len(str(n)):
#     sum=sum+int(n[i])
#     i+=1
# if int(n)%sum==0:
#     print(n,"harshad number")
# else:
#     print(n,"not harshad number")
    
n=(input("enter number:"))
i=0
sum=0
while i<len(str(n)):
    sum=sum+int(n[i])
    i+=1
if int(n)%sum==0:
    print(sum,n,"harshad number")
else:
    print(sum,n,"not hrshad number")
    
