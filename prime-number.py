import math

print("1부터 100 사이의 소수 (최적화 버전):")

for num in range(2, 101):
    is_prime = True

    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        