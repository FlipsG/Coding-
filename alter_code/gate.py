def and_gate(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

# Testen des AND-Gatters
input1 = 1
input2 = 0
result = and_gate(input1, input2)
print(f"Das Ergebnis des AND-Gatters für {input1} und {input2} ist: {result}")


def or_gate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

# Testen des OR-Gatters
input1 = 1
input2 = 0
result = or_gate(input1, input2)
print(f"Das Ergebnis des OR-Gatters für {input1} und {input2} ist: {result}")


def not_gate(a):
    if a == 1:
        return 0
    else:
        return 1

# Testen des NOT-Gatters
input1 = 1
result = not_gate(input1)
print(f"Das Ergebnis des NOT-Gatters für {input1} ist: {result}")


def and_gate(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def not_gate(a):
    if a == 1:
        return 0
    else:
        return 1

def nand_gate(a, b):
    and_result = and_gate(a, b)
    nand_result = not_gate(and_result)
    return nand_result

# Testen des NAND-Gatters
input1 = 1
input2 = 0
result = nand_gate(input1, input2)
print(f"Das Ergebnis des NAND-Gatters für {input1} und {input2} ist: {result}")


def or_gate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def not_gate(a):
    if a == 1:
        return 0
    else:
        return 1

def nor_gate(a, b):
    or_result = or_gate(a, b)
    nor_result = not_gate(or_result)
    return nor_result

# Testen des NOR-Gatters
input1 = 1
input2 = 0
result = nor_gate(input1, input2)
print(f"Das Ergebnis des NOR-Gatters für {input1} und {input2} ist: {result}")


def xor_gate(a, b):
    if (a == 1 and b == 0) or (a == 0 and b == 1):
        return 1
    else:
        return 0

# Testen des XOR-Gatters
input1 = 1
input2 = 0
result = xor_gate(input1, input2)
print(f"Das Ergebnis des XOR-Gatters für {input1} und {input2} ist: {result}")


def xnor_gate(a, b):
    if (a == 1 and b == 1) or (a == 0 and b == 0):
        return 1
    else:
        return 0

# Testen des XNOR-Gatters
input1 = 1
input2 = 0
result = xnor_gate(input1, input2)
print(f"Das Ergebnis des XNOR-Gatters für {input1} und {input2} ist: {result}")
