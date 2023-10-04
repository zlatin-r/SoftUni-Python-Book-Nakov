while True:
    try:
        n = int(input("Enter even number: "))
        if n % 2 == 0:
            print("Even number entered:", + n)
            break
    except ValueError:
        print("Invalid number")
