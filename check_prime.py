# checkout prime 
def check_prime(a):
    number_type = "Prime"
    for i in range(2, a):
        if a % i == 0:
            number_type = "Not-prime"
    return number_type        

print(check_prime(45))

# check odd and even number
def check_odd_even(a):
    if a % 2 == 0:
        return "even number"
    else:
        return "odd number"

print(check_odd_even(10))  
print(check_odd_even(15))  
    
# Function to check if a number is an Armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == num

# --- Part 1: Check a single number ---
number = int(input("Enter a number to check: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")

print(is_armstrong(15))    