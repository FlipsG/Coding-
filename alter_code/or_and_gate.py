def or_gate(a, b):
    return a or b

def and_gate(a, b):
    return a and b

# Simulating a more complex logic circuit
input1 = int(input("Sensor 1 (Motion Detected - 0 or 1): "))
input2 = int(input("Sensor 2 (Heat Detected - 0 or 1): "))
input3 = int(input("Keypad (Correct Code - 0 or 1): "))

# Logic for vault access
motion_or_heat = or_gate(input1, input2)
security_check = and_gate(motion_or_heat, input3)

if security_check:
    print("Vault access granted. The vault is open.")
else:
    print("Access denied. The vault remains closed.")