# Ejercicios para demostrar fallos controlados

Este archivo propone escenarios simples para usar durante una clase. El código
inicial del proyecto está correcto; estas modificaciones son temporales y deben
revertirse después de la demostración.

## Escenario 1 - Test fallido

Objetivo: mostrar cómo un cambio incorrecto hace fallar un test.

1. Abrir `calculadora/operaciones.py`.
2. Cambiar temporalmente la función `sumar(a, b)`:

```python
def sumar(a: float, b: float) -> float:
    return a - b
```

3. Ejecutar:

```bash
pytest
```

Debería fallar el test `test_sumar_dos_numeros`, porque espera que `2 + 3` sea
igual a `5`.

En GitHub Actions debería obse-rvarse que el paso `Ejecutar tests` falla. El
registro del workflow mostrará el test fallido y la diferencia entre el valor
esperado y el valor obtenido.

Para revertirlo, restaurar la función:

```python
def sumar(a: float, b: float) -> float:
    return a + b
```

## Escenario 2 - Error de calidad

Objetivo: mostrar cómo Ruff detecta problemas simples de calidad de código.

1. Abrir `calculadora/operaciones.py`.
2. Agregar esta línea al inicio del archivo:

```python
import math
```

3. Ejecutar:

```bash
ruff check .
```

Ruff debería informar un error `F401`, porque `math` fue importado pero no se
usa.

En GitHub Actions debería fallar el paso `Analizar calidad del código`.

Para revertirlo, eliminar la línea:

```python
import math
```

## Escenario 3 - Nuevo test

Objetivo: mostrar cómo agregar una verificación nueva al conjunto de tests.

El proyecto ya incluye un test de división por cero. Para practicar, se puede
agregar otro test con una comprobación explícita del tipo de excepción.

1. Abrir `tests/test_operaciones.py`.
2. Agregar al final:

```python
def test_dividir_por_cero_error_explicito() -> None:
    with pytest.raises(ValueError):
        dividir(25, 0)
```

3. Ejecutar:

```bash
pytest
```

El nuevo test debería pasar, porque `dividir()` ya controla la división por cero.
Si la función no lanzara `ValueError`, el test fallaría y GitHub Actions lo
mostraría en el paso `Ejecutar tests`.

## Escenario 4 - Pull Request

Objetivo: mostrar cómo GitHub Actions se ejecuta automáticamente al abrir un
Pull Request.

1. Crear una rama:

```bash
git checkout -b clase/demo-actions
```

2. Realizar una modificación pequeña, por ejemplo agregar un test o cambiar un
mensaje del README.

3. Confirmar los cambios:

```bash
git add .
git commit -m "Demostración de GitHub Actions"
```

4. Subir la rama a GitHub:

```bash
git push -u origin clase/demo-actions
```

5. Crear un Pull Request desde GitHub.

Al crear el Pull Request, GitHub Actions debería ejecutar automáticamente el
workflow. En la pestaña del Pull Request se podrá observar si los pasos de Ruff,
pytest y cobertura terminan en `OK` o en `ERROR`.
