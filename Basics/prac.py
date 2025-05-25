# # wap to sum two nos
# x= int(input("enter no1:"))
# y= int(input("enter no1:"))
# print("The sum is:" ,x+y)

# wap to print multiples of no
# x= int(input("enter no:"))
# for i in range(1,11):
#     print (x*i)

#wap to print the pattern using for loop
# n=11
# for i in range (1,7):
#     for j in range(1,i):
#         print("*", end="")
#     print("")

#wap to calc the no of spacees in a sentance 
# c=0
# x= input("enter:")
# for i in x:
#     if i==" ":
#         c+=1
# print("the number of spaces is:" ,c)

# or
# x=input("enter:")
# b=x.count(" ")
# print(b)

# # wap to store 10 numbered elements in an list and disp that back
# l=[]
# for i in range(10):
#     l.append(input("enter:"))
#     print(l)
   

#prime or not 
# x=int(input("enter no:"))
# flag = "false"
 
# for i in range(2,x):
#     if (x%i==0):
#         flag = ""
#         break
#     else:
#         print("it is prime")

# wap to print diamond wala star 
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()
