# Q1)
def reverse_list(l):
    return l[::-1]
l = [1,2,3,4,5]
print(reverse_list(l))

# Q2)
def count_occurences(l, n):
    return l.count(n)
l = [1,2,3,4,5,1,2,3,4,5]
n = 1
print(count_occurences(l, n))

# Q3)
def contains_duplicates(l):
    return len(l) != len(set(l))
l = [1,2,3,4,5]
print(contains_duplicates(l))

# Q4)
def find_missing(l):
    return 18 - sum(l)
l = [1,2,3,4,5]
print(find_missing(l))

# Q5)
def replace_odd(l):
    return [-1 if n % 2 != 0 else n for n in l]
l = [1,2,3,4,5]
print(replace_odd(l))