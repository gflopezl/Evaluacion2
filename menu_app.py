# Función para agregar una compra a la lista de compras
def agregar_compra(compras, total_compras):
    precio = float(input("Ingrese el precio del producto: "))
    compras.append(precio)
    total_compras += precio
    print("Compra agregada correctamente.")
    return total_compras

# Función para mostrar las compras registradas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras registradas:")
        for i, (precio) in enumerate(compras, 1):
            print(f"Compra {i}: ${precio:.2f}")

# Función para mostrar el total gastado formateado como valor monetario
def mostrar_total(total_compras):
    print(f"Total gastado: ${total_compras:.2f} ")

# Función principal del programa
def main():
    compras = []
    total_compras = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            total_compras =agregar_compra(compras, total_compras)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(total_compras)
        elif opcion == '4':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()