def and_gate(a, b):
    return a and b

# Simulating a basic logic circuit
input1 = int(input("Switch 1 (0 or 1): "))
input2 = int(input("Switch 2 (0 or 1): "))

# Logic for turning on the lightbulb
output = and_gate(input1, input2)

if output:
    print("The lightbulb is ON.")
else:
    print("The lightbulb is OFF.")
