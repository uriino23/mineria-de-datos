eleccionTipoPizza = input("Bienvenido. Escoge una opcion:Vegetariana (v) No vegetariana (nv)")
if eleccionTipoPizza == "v":
    eleccionIngrediente = input("Escoge una opcion: Pimiento (p) Tofu (t)")
    if eleccionIngrediente == "p":
        print("Escogiste una pizza vegetariana con pimiento, mozzarella y tomate ")
    elif eleccionIngrediente == "t":
        print("Escogiste una pizza vegetariana con Tofu, mozzarella y tomate.")
elif eleccionTipoPizza == "nv":
    eleccionIngrediente = input("Escoge una opcion: Peperoni (p) Jamon (j) Salmon (s)")
    if eleccionIngrediente == "p":
        print("Escogiste una pizza no vegetariana con Peperoni, mozzarella y tomate.")
    elif eleccionIngrediente == "j":
        print("Escogiste una pizza no vegetariana con Jamón, mozzarella y tomate.")
    elif eleccionIngrediente == "s":
        print("Escogiste una pizza no vegetariana con Salmón, mozzarella y tomate.")