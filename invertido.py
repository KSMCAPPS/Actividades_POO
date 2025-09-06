num = int(input("Introduce un número: "))
invertido = 0

if num <=0:
    print("Ingresa un número mayor a cero")
else: 
    
# // elimina numeros con division entera
    while num > 0:
        invertido = invertido * 10 + num % 10
        num = num // 10

print("Número invertido:", invertido)
