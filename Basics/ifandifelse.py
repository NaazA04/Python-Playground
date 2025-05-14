# Q1
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# Q2
x=int(input("enter number:"))
if x<=999: 
    print("it is a 3-digit number ")
else: 
    print("it is not a 3-digit number ")

# Q3
x=int(input("enter age:"))
if x>= 18: 
    print("eligible")
else:
print("not eligible")


# Q4
x=int(input("enter number"))
if x%10==3: 
    print("The last digit is 3")
else:
    print("no")

# Q5
x= input("enter alphabet:")
if x=="a" or x=="e" or x=="i"or x=="o" or x=="u" or x=="A" or x=="E"or x=="I "or x=="O" or x== "U": 
    print("Its a vowel")
else:
    print("its a consonant")

# Q6
x= int(input("enter month number"))
if x == "1" or x== "3" or x== "5" or x== "7" or x== "8" or x== "10" or x== "12":
    print("It has 31 days")
elif x=="2":
    print("It has 28 or 29 days")
else:
    print("It has 30 days")


# Q7
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a == b == c:
    print("Equilateral triangle")
elif a != b and b != c and a != c:
    print("Scalene triangle")
else:
    print("Isosceles triangle")

# # Q8
bill=0
x=int(input("enter no. of units:"))
if x<=100: 
   bill=0
elif x<=200: 
    bill= (x-100)*5
else: 
     bill = (100 * 5) + (x - 200) * 10

print("Total bill amount is Rs", bill")

# #Q9
y=0
x= (int(input('enter cost')))
if x>100000:
    y=x*15/100
elif x>50000 and x<= 100000:
    y=x*10/100
else:
    y=x*5/100
print("Road tax to be paid is", y)

#Q10
discount=0
netamt=0
x=int(input("enter market price:"))
if x>1000:
    discount= 0.2
    netamt= x-discount
elif x>7000 and x<=10000:
    discount= 0.15
    netamt= x-discount
else: 
    discount=0.1
    netamt= x-discount

print('Net Amount=',netamt)
