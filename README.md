# calculadora-ci

`calculadora-ci` es un proyecto educativo pequeño para estudiantes de Ingeniería
de Software II. Su objetivo principal es practicar testing automatizado,
integración continua y GitHub Actions con un repositorio fácil de entender y
modificar durante una clase.

La aplicación implementa una calculadora simple con funciones de suma, resta,
multiplicación, división, potencia y cálculo de porcentaje.

## 1. Objetivo del proyecto

Este repositorio fue creado para aprender:

- testing automatizado con `pytest`;
- medición de cobertura con `pytest-cov`;
- análisis de calidad con `ruff`;
- integración continua con GitHub Actions.

La intención no es construir una aplicación compleja, sino tener una base clara
para demostrar cómo se ejecutan verificaciones automáticas cada vez que cambia el
código.

## 2. Instalación

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Activar el entorno virtual en Windows CMD:

```bat
venv\Scripts\activate.bat
```

Activar el entorno virtual en Linux/macOS:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 3. Ejecutar aplicación

```bash
python main.py
```

## 4. Ejecutar tests

```bash
pytest
```

## 5. Ejecutar cobertura

```bash
pytest --cov=calculadora
```

## 6. Ejecutar Ruff

```bash
ruff check .
```

## 7. GitHub Actions

Cada `push` o `Pull Request` dispara automáticamente el workflow definido en
`.github/workflows/tests.yml`.

Flujo conceptual:

```text
Push / Pull Request
|
v
GitHub Actions
|
+-- Ruff
|
+-- Pytest
|
+-- Cobertura
|
v
OK / ERROR
```

Si todas las verificaciones pasan, el workflow finaliza correctamente. Si alguna
verificación falla, GitHub Actions marca el proceso como fallido y muestra el
paso donde ocurrió el error.
