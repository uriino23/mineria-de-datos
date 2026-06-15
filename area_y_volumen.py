def area_circulo(radio):  # pi * r**2
    return 3.14 * radio * radio

def volumen_cilindro(radio, altura):  # V=pi r**2 *h
    return area_circulo(radio) * altura

r = float(input("Ingresa el radio: "))
h = float(input("Ingresa la altura: "))
print("Área del círculo:", area_circulo(r))
print("Volumen del cilindro:", volumen_cilindro(r, h))