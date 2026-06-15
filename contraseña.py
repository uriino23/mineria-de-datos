contraseña = "I123Y"
while True:
    usuario = input("Ingresar contraseña: ")
    if usuario == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo")