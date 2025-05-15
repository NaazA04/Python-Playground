# Q1 
x=int(input("enter number: "))
for i in range(1,11):
    print(f"{x} x {i} = {x * i}")
    i+=1 

# Q2 
count = 0
x = int(input("Enter number: ")) 
if x == 0:
    count = 1
else:
    while x > 0: 
        x = x // 10  
        count += 1    
print("Total no. of digits =", count)
# Q3
x=eval(input("Enter list:"))
i = len(x) - 1
while i >= 0:
    print(x[i])
    i -= 1  

# Q4
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue  
    is_prime = True  
    for i in range(2, num):
        if num % i == 0:  
            is_prime = False  
            break  

    if is_prime:  
        print(num)  

# Q5
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

# Q6
n = int(input())
num = str(n)
result = int(num[::-1])
print(result)

# Q9 (a)
n = 5  
for i in range(n, 0, -1):  
    for j in range(i, 0, -1): 
        print(j, end=" ")  
    print()

# Q9 (b)
n = 5  
for i in range(1, n + 1):  
    for j in range(i):
        print("*", end=" ") 
    print()  

for i in range(n - 1, 0, -1):  
    for j in range(i):  
        print("*", end=" ") 
    print() 
