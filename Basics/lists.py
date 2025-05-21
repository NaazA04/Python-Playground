# Q1
l=eval(input("enter:"))
for i in l:
    if l.count(i) == 2:
        l.remove(i)
print(l)

#Q2
x=eval(input("enter first list:"))
y=eval(input("enter second list:"))
for i in x:
    for j in y:
        if i==j:
            print("True")
            break

#Q3
l=eval(input("enter:"))
for i in l:
    if i%2==0:
        l.remove(i)
print(l)

#Q4
l=eval(input("enter:"))
l.sort()
print(l[1])

#Q5
lst=eval(input("enter:"))
n=int(input("enter n:"))
result = []
for i in range(0, len(lst), n):
    result.append(lst[i:i + n])
print(result)

#Q6
def union_intersection(list1, list2):
    union = list1 + list2
    intersection = []
    for i in list1:
        if i in list2:
            intersection.append(i)
    return union, intersection
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print(union_intersection(list1, list2))

# Q7
def palindrome(list):
    return list == list[::-1]
list = [1, 2, 3, 2, 1]
print(palindrome(list))