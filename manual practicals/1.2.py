def check_number(x):
    if x > 0:
        print("Positive number")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def countdown(n):
    while n > 0:
        print(n)
        n -= 1

def main():
    num = int(input("Enter a number: "))
    check_number(num)
    print("Numbers from 1 to 5:")
    print_numbers(5)
    print("Countdown from 5:")
    countdown(5)

main()
