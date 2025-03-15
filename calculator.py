first = float(input("First number: "))
second = float(input("Second number: "))

mode = input("Choose an operator (+, -, *, /, ^): ")

if mode == "+":
    sum = first + second
    print(sum)
elif mode == "-":
    sum = first - second
    print(sum)
elif mode == "*":
    sum = first * second
    print(sum)
elif mode == "/":
    sum = first / second
    print(sum)
elif mode == "^":
    sum = first ** second
    print(sum)
else:
    print("invalid choice.")
