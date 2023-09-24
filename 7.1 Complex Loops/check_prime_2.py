n = int(input())
is_prime = True

if n <= 1:
    is_prime = False

for i in range(2, n - 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")