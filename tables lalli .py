# n=int(input("enter any number"))
# i=1
# while i<=n:
#     j=n
#     while j>=i:
#         print("*",end=" ")
#         j-=1
#     print()
#     i+=1



# i=0
# j=1
# while i<=10:
#     print(i)
#     print(j)
#     i=i+j
#     j=j+i

# a=1
# b=5
# i=1
# while i<=b*2:
#     if i<4:
#         print(("H"*a))
#         a+=1
#     else:
#         print(('H'*a))
#         a=a-1
#     i+=1

# n=int(input("enter any number of rows:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
        
#     for j in range(i,-1,-1):
#         print(j+1, end=" ")
#     print()

# def dic_squa(num):
#     i=1
#     while i<=num:
#         dic[i]=i*i
#         i+=1
# dic={}
# dic_squa(15)       
# print(dic)

# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': [ 'subj1','subj2']}
# count=0
# for x in dict:
#     if isinstance(dict[x],list):
#         count+=len(dict[x])
# print("total count:",count)

# n=int(input("enter number of rows:"))
# for i in range(n):
#    for j in range(n-i):
#       print(j+1,end=" ")
#    print()

# a="mississippi"
# b={}
# i=0
# while i<len(a):
#     count=0
#     j=0
#     c={}
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     #if b not in c:
#         #print("dfg")
#         #c[i]=b[i]
#     b[a[i]]=count
#     i=i+1
# print(b)

# num=int(input("enter any number"))
# power=0
# string=""
# while(num>0):
#     string=string+("0"*power)+str(num%10)+"+"
#     num=num//10
#     power=power+1
# string=string[:-1]
# print(string[::-1])
# Footer
# © 2022 GitHub, Inc.

# n=int(input("enter your number:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("2",end=" ")
#         j=j+1
#     print(",",end=" ")
#     i+=1

# a=9119
# b=str(a)
# i=0
# while i<len(b):
#     print(int(b[i])**2,end="")
#     i+=1

# print("WELCOME TO THE BIRTHDAY PARTY")
# age=9
# can_height=[1,3,4,6,4,6]
# can_height.sort()
# # pprint(can_height)
# max=0
# i=0
# while i<len(can_height):
#     c=0
#     if can_height[i]>max:
#         max=can_height[i]
#     i+=1
#     for ele in can_height:
#         if ele==max:
#             c+=1
# print("Tallest Candle is:",max)
# print("Number Of Candle is:",c)

# list_a=[5,6,9,10,2]
# sum=0
# i=0
# while i<len(list_a):
#     sum+=list_a[i]
#     i+=1
# print(sum)

# a="mississippi"
# b={}
# i=0
# while i<len(a):
#     count=0
#     j=0
#     c={}
#     while j<len(a):
#         if a[i]==a[j]:
#             count=count+1
#         j=j+1
#     #if b not in c:
#         #print("dfg")
#         #c[i]=b[i]
#     b[a[i]]=count
#     i=i+1
# print(b)

# my_dict = {'a':50, 'b':58, 'c': 56,'d':40, 'e':100, 'f': 20}  
# list=[]
# max1=0
# max2=0
# max3=0
# for key in my_dict:
#     for value in my_dict:
#         if my_dict[key]>max1:
#             max1=my_dict[key]
#         elif max1>my_dict[value] and max2<my_dict[value]:
#             max2=my_dict[value]
#         elif max2>my_dict[value] and max3<my_dict[value]:
#             max3=my_dict[value]
# list.append(max1)
# list.append(max2)
# list.append(max3)
# print(list)


def dic_squares(num):
    i=1
    while i<=num:
        dic[i]=[i*i]
        i=i+1
dic={}
dic_squares(15)       
print(dic)


