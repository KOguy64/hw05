def calculate(a, operator, b):
    if operator == "+":
        return a+b
    if operator == "-":
        return a-b
    if operator == "*":
        return a*b
    if operator == "/":
        if b == 0:
            return None
        return a/b
    else:
        return None

def main():
    while True:
        first_input = input("First number (or q):")
        if first_input == "q":
            break
        a = float(first_input)
        operator = input("Operator (+ - * /):")
        b = float(input("Second number: "))
        result = calculate(a, operator, b)
        if result == None:
            print("Cannot calculate that")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()