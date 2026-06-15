def total_factura(cantidad, iva=21):
    total = cantidad + (cantidad * iva / 100)
    return total
cantidad = float(input("Ingresa la cantidad sin IVA: "))
print("Total con IVA:", total_factura(cantidad))