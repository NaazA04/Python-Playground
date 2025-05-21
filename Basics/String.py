#1 
s = input("Enter a string: ")
if s == s[::-1]:
    print(f"The string '{s}' is a palindrome.")
else:
    print(f"The string '{s}' is not a palindrome.")

n = len(s)
if n % 2 == 0:
    first_half = s[:n//2]
    second_half = s[n//2:]
else:
    first_half = s[:n//2]
    second_half = s[n//2+1:]  

if first_half == second_half:
    print(f"The string '{s}' is symmetrical.")
else:
    print(f"The string '{s}' is not symmetrical.")

#2
s = input("Enter a string: ")
count = 0
for char in s:
    count += 1
print(f"The length of the string is: {count}")


#3
string = "hello, world People!"
unique_chars = set()
result = ""
for char in string:
    if char not in unique_chars:
        unique_chars.add(char)
        result += char
print("The string without duplicates is:", result)

#4
string = "Hi, How Are You?"
char_counts = {}
for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1
max_char = max(char_counts, key=char_counts.get)
print("The maximum frequency character is:", max_char, "with frequency:", char_counts[max_char])

#5
string = "Im Good Thank you"
char_counts = {}
for char in string:
    char_counts[char] = char_counts.get(char, 0) + 1
print("Character counts:", char_counts)

#6
string = "Eat oranges 123@#$%"
letters = 0
digits = 0
symbols = 0
for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print("Letters:", letters, "Digits:", digits, "Symbols:", symbols)

#7
email_addresses = ["user1@itm.edu", "user2@gmail.com", "user3@itm.edu", "user4@yahoo.com"]

for email in email_addresses:
    if not email.endswith("@itm.edu"):
        print(f"Email {email} is not from @itm.edu. Moving to spam.")
    else:
        print(f"Email {email} is from @itm.edu. Keeping in inbox.")

#8
password = "Lalala123!"

if len(password) < 8:
    print("Password is invalid: Must be at least 8 characters long.")
elif not re.search(r"([A-Z])", password):
    print("Password is invalid: Must contain at least one uppercase letter.")
elif not re.search(r"([a-z])", password):
    print("Password is invalid: Must contain at least one lowercase letter.")
elif not re.search(r"([!#$%&*+--?-])", password):
    print("Password is invalid: Must contain at least one special character.")
else:
    print("Password is valid.")
