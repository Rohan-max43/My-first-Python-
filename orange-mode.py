# I'm orange mode

# Even or Odd
# Write a program that takes a number as input and prints whether it is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "even number"
    else:
        return "odd number"
    
print(check_even_odd(32))

# Sum of Digits
# Write a program that finds the sum of digits of a num
def sum_of_num(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total

print(sum_of_num(55))

# Palindrome Check
# Write a function to check if a string is a palindrome.
# Example: "madam" → True, "hello" → False
def palindrome_check(s):
    s = s.lower()
    if s [::-1] == s:
        return "palindrome"
    else:
        return "Not plaindrom"

print(palindrome_check("Madam"))

# Factorial Calculation
# Write a recursive function to calculate the factorial of a number.
def factorial_calculation(n):
    total = 1
    for num in range(1, n +1):
        total *= num
    return total    

print(factorial_calculation(5))

# Check Amstrong number
def amstrong_number(n):
    total = 0
    power = len(str(n))
    for i in str(n):
        total += int(i)**power

    if total == n:
        return "Amstrong number"
    else:
        return "Not Amstrong number"    
    
print(amstrong_number(153))

# Prime Numbers in Range
# Write a program to print all prime numbers between 1 and 100.

def prime_check(n):
    number_type = "Prime"
    for num in range(2, n):
        if n % num == 0:
            number_type = "Not Prime"
    return number_type

result = prime_check(12)
print(result)

count = 0
for i in range(1, 100):
    result = prime_check(i)
    if result == "Prime":
        count += 1

print(count)

# Anagram Checker
# Write a function to check if two words are anagrams.
# Example: "listen" & "silent" → True
def anagram_check(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return False
    
    temp_word2 = list(word2)
    for letter in word1:
        if letter in word2:
            temp_word2.remove(letter)
        else:
            return "Not Anagram"
    return "Anagram"        

print(anagram_check("hello", "world"))  
print(anagram_check("listen", "silent"))
