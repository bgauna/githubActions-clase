import pytest
import math

from calculadora.operaciones import (
    dividir,
    multiplicar,
    porcentaje,
    potencia,
    restar,
    sumar,
)


def test_sumar_dos_numeros() -> None:
    assert sumar(2, 3) == 5


def test_sumar_numeros_negativos() -> None:
    assert sumar(-2, -3) == -5


def test_restar_dos_numeros() -> None:
    assert restar(10, 4) == 6


def test_restar_cero() -> None:
    assert restar(8, 0) == 8


def test_multiplicar_dos_numeros() -> None:
    assert multiplicar(4, 5) == 20


def test_multiplicar_por_cero() -> None:
    assert multiplicar(9, 0) == 0


def test_dividir_dos_numeros() -> None:
    assert dividir(10, 2) == 5


def test_dividir_numeros_decimales() -> None:
    assert dividir(5, 2) == pytest.approx(2.5)


def test_dividir_por_cero_lanza_error() -> None:
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_potencia() -> None:
    assert potencia(2, 3) == 8


def test_potencia_con_exponente_cero() -> None:
    assert potencia(7, 0) == 1


def test_porcentaje() -> None:
    assert porcentaje(200, 10) == 20


def test_porcentaje_decimal() -> None:
    assert porcentaje(80, 12.5) == pytest.approx(10)
