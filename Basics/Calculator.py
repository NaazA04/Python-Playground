# #makeacalculator
# a=int(input("enter number:"))
# b=int(input("enter number:"))
# multiplication=a*b
# division=a/b
# modulus=a%b
# subtraction= a-b 
# addition= a+b
# floordiv=a//b
# print("Division=",division)
# print("Multiplication=",multiplication)
# print("modulus=",modulus)
# print("addition=",addition)
# print("subtraction=",subtraction)
# print("Floor Division=",floordiv)

# #continue statement example 
# for i in range (12):
#     if(i==10):
#         print("skip the iteration")
#         continue 
#     print("5 X",i,"=",5*i)
# #do-while loop syantx 
# #     do{
#            #loop body;
# #     }while(condition);



def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print("prime:",isprime(17))

#Fibonacci series
def fs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fs(n-1)+fs(n-2)
print(fs(6))

#fac
def fac(n):
    if (n==1 or n==0):
        return 0
    else:
        return n*fac(n-1)
print(fac(5))

#aplindrome
def palin(s):
    return s== s[::-1]
print("palindrome:",palin("madam"))

#sum of var lenghth argument
def total(*args):
    return sum(args)
print("sum:",total(1,2,3,4))

#remove duplicates from a list
l=[2,2,3,4,5,5]
newl=list(set(l))
print(newl)

#square of nos using list comprehesion
sq=[x**2 for x in range(1,11)]
print(sq)

#print element wise tuples
t=[(1,2,3),(4,5,6),(3,4,8)]
r=tuple(map(sum,zip(*t)))
print(r)

#unique item from a set
s1={1,2,3}
s2={2,3,5}
unique=s1.symmetric_difference(s2)
print(unique)

#dic comprehension for even ages
og={"jack":34,"mick":45,"laz":66}
new={k:v for k,v in og.items() if v%2==0}
print(new)

#removing spaces in string
x= " Hi welocme to python"
y=x.replce(" ","")
print(y)

#circle class with area and perimeter
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14* self.radius**2
    def peri(self):
        return 2*3.14*self.radius
c=circle(5)
print(c.area())
print(c.perimeter())

#inheritance and class
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class student(person):
    def __init__(self,n,a,r,s):
        super().__init__(n,a)
        self.rollno= r
        self.stream=s

    def display(self):
        print("name:",self.name,"age",self.age,"rollno",self.rollno,"stream:",self.stream)

s=student("alice",10,101,"science")
s.display()


#count words in a textfile
with open("textfile.txt","r") as file:
    content=file.read()
    count=len(content.split())
print(count)

#exception handling 
try:
    x=9/0
except ZeroDivisionError:
    print("division by zero is not possible")

#lambda fn in map()
n=[1,2,3]
s=list(map(lambda x:x**2,n))
print(s)

#lamda in filter()
n=[2,4,5,67,7]
x=list(filter(lambda x:x%2==0,n))
print(x)

#class and static method 
class ex:
    def __init__(self,value):
        self.value=value
    
    #class meth
    def classmeth(cls):
        print("this is class meth")
    
    #static meth
    def stat():
        print("this is static method")
ex.classmeth()
ex.stat()


import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result.set(num1 + num2)

root = tk.Tk()
root.title("Add Numbers")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)
label_result.pack()

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.pack()

root.mainloop()


original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_age_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}
print("Even age dict:", even_age_dict)


arr = [1, 2, 3, 4, 5]
total = sum(arr)
average = total / len(arr)
print("Sum:", total, "Average:", average)