def main():
    print("Welcome to my calculator!")
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        choice = input("What operation would you like to do? (add, subtract, multiply, divide): ")
        if choice == 'add':
            print(num1 + num2)
        elif choice == 'subtract':
            print(num1 - num2)
        elif choice == 'multiply':
            print(num1 * num2)
        elif choice == 'divide':
            print(num1 / num2)
        else:
            print("Invalid input. Please try again.")
main()