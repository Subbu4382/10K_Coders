
# Q1: Multiplication Table (1 to 10)
print("Multiplication Table (1 to 10)")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# Q2: Count Prime Numbers in a Range (1 to 100)
print("Count Prime Numbers in a Range (1 to 100)")
prime_count = 0
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
print("Total prime numbers between 1 and 100:", prime_count)

# Q3: Print All Pairs of Numbers (1 to n) Where Sum is Even
print("Print All Pairs of Numbers (1 to n) Where Sum is Even")
n = int(input("Enter a number:"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            print(f"({i},{j})")

# Q4: Count Total Factors of All Numbers from 1 to n
print("Count Total Factors of All Numbers from 1 to n")
n = int(input("Enter a number:"))
total_factors = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total_factors += 1
print("Total number of factors from 1 to", n, "is:", total_factors)

# Q5: Print All Pythagorean Triplets with Values ≤ n
print("Print All Pythagorean Triplets with Values ≤ n")
n = int(input("Enter a number:"))
for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            if a * a + b * b == c * c:
                print(f"({a}, {b}, {c})")
