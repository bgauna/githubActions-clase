from calculadora.operaciones import (
    dividir,
    multiplicar,
    porcentaje,
    potencia,
    restar,
    sumar,
)


def pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


def mostrar_menu() -> None:
    print("Calculadora CI")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Porcentaje")


def main() -> None:
    operaciones = {
        "1": (
            "Suma",
            sumar,
            "Ingrese el primer número: ",
            "Ingrese el segundo número: ",
        ),
        "2": (
            "Resta",
            restar,
            "Ingrese el primer número: ",
            "Ingrese el segundo número: ",
        ),
        "3": (
            "Multiplicación",
            multiplicar,
            "Ingrese el primer número: ",
            "Ingrese el segundo número: ",
        ),
        "4": (
            "División",
            dividir,
            "Ingrese el dividendo: ",
            "Ingrese el divisor: ",
        ),
        "5": ("Potencia", potencia, "Ingrese la base: ", "Ingrese el exponente: "),
        "6": (
            "Porcentaje",
            porcentaje,
            "Ingrese el valor base: ",
            "Ingrese el porcentaje: ",
        ),
    }

    mostrar_menu()
    opcion = input("Seleccione una operación: ")

    if opcion not in operaciones:
        print("Opción inválida.")
        return

    nombre, operacion, mensaje_a, mensaje_b = operaciones[opcion]
    a = pedir_numero(mensaje_a)
    b = pedir_numero(mensaje_b)

    try:
        resultado = operacion(a, b)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"{nombre}: {resultado}")


if __name__ == "__main__":
    main()
