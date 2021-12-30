#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
#Python ya tiene una función max()
def max(num1, num2):
    if (num1 > num2):
        mayor = num1
    elif (num1 < num2):
        mayor = num2
    else:
        mayor = "Son iguales"
    return mayor

print(max(2,4))
print(max(-1,0))
print(max(10, 9))
print(max(10, 10))