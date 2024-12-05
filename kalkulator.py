import os 

os.system("clear")

print("kalkulator mewing")
a = float(input("angka : "))
b = float(input("angka : "))
c = input("+ atau - : ")


print(a+b) if c == "+" else print(a-b)
