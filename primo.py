numero = int(input("Ingresa un número entero: "))
if numero > 1:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
else:
    print("El número no es primo")