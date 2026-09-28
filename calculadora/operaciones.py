"""Operaciones matemáticas simples para la calculadora."""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a - b


def restar(a: float, b: float) -> float:
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve la multiplicación de dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Devuelve la división de dos números.

    Lanza ValueError si el divisor es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")

    return a / b


def potencia(a: float, b: float) -> float:
    """Devuelve el resultado de elevar a a la potencia b."""
    return a**b


def porcentaje(valor: float, porcentaje_calculado: float) -> float:
    """Calcula un porcentaje sobre un valor."""
    return valor * porcentaje_calculado / 100
