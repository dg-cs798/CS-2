import math
print("Many of things you can do:\n")

print("add")
print("subtract")
print("multiply")
print("divide")
print("floored division")
print("mod")
print("power")
print("square root\n")
print("round up")
print("round down")

op_selected = input("What would you like to do? ")

first_num = float(input("\nEnter first num:"))
if op_selected != "square root" and op_selected != "round up" and op_selected != "round down":
    second_num = float(input("Enter second num:"))


if op_selected == "add":
    print(f"{first_num} + {second_num} = {first_num + second_num:.2f}")
elif op_selected == "subtract":
    print(f"{first_num} - {second_num} = {first_num - second_num:.2f}")
elif op_selected == "multiply":
    print(f"{first_num} * {second_num} = {first_num * second_num:.2f}")
elif op_selected == "divide":
    print(f"{first_num} / {second_num} = {first_num / second_num:.2f}")
elif op_selected == "floored division":
    print(f"{first_num} // {second_num} = {first_num // second_num}")
elif op_selected == "mod":
    print(f"{first_num} % {second_num} = {first_num % second_num}")
elif op_selected == "power":
    print(f"{first_num} ^ {second_num} = {first_num ** second_num}")
elif op_selected == "square root":
    print(f"{first_num} squared = {math.sqrt(first_num):.2f}")
elif op_selected == "round up":
    print(f"{first_num} rounded up = {math.ceil(first_num):.2f}")
elif op_selected == "round down":
    print(f"{first_num} rounded down = {math.floor(first_num):.2f}")
else:
    print("Sorry, Operation not available.")
    
    
    
    