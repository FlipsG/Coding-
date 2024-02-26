def and_gate(a, b):
    return a and b

# Simulating an AND gate with user input
input1 = int(input("Enter first input (0 or 1): "))
input2 = int(input("Enter second input (0 or 1): "))

result = and_gate(input1, input2)
print(f"The result of the AND gate for inputs {input1} and {input2} is: {result}")
