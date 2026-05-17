# Curso Automation - Pruebas E2E con Selenium

Proyecto de automatización de pruebas para el sitio [SauceDemo](https://www.saucedemo.com), desarrollado como parte de un curso de automatización de pruebas con Python, Selenium y Pytest.

## 📋 Propósito

El proyecto valida las funcionalidades principales de la aplicación web **Swag Labs** (SauceDemo), cubriendo los siguientes flujos:

- **Login:** Validación del formulario, carga de elementos y autenticación exitosa.
- **Inventario:** Verificación del título, listado de productos e interfaz de usuario.
- **Carrito de compras:** Agregar productos, contador del carrito y navegación al carrito.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Versión | Descripción |
|---|---|---|
| Python | 3.x | Lenguaje base del proyecto |
| Selenium | 4.44.0 | Automatización del navegador web |
| pytest | 9.0.3 | Framework de ejecución de pruebas |
| pytest-html | 4.2.0 | Generación de reportes HTML |
| ChromeDriver | (automático) | Driver para Google Chrome (gestionado por Selenium Manager) |

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/pancho260/Curso-Automation
cd "Curso Automation"
```

### 2. Crear y activar un entorno virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar en Windows
.venv\Scripts\activate

# Activar en macOS/Linux
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install selenium pytest pytest-html
```

> **Nota:** ChromeDriver se gestiona automáticamente mediante **Selenium Manager** (incluido en Selenium 4.x). Solo necesitas tener Google Chrome instalado.

---

## ▶️ Ejecución de pruebas

### Ejecutar todas las pruebas con reporte HTML

```bash
python -m pytest -v --html=reporte.html
```

### Ejecutar un módulo específico

```bash
# Solo pruebas de login
python -m pytest src/test/test_login.py -v --html=reporte.html

# Solo pruebas de inventario
python -m pytest src/test/test_inventory.py -v --html=reporte.html

# Solo pruebas del carrito
python -m pytest src/test/test_cart.py -v --html=reporte.html
```

### Ver el reporte

Después de ejecutar las pruebas, abre el archivo generado `reporte.html` en tu navegador para ver los resultados detallados.

---

## 📁 Estructura del proyecto

```
Curso Automation/
├── src/
│   └── test/
│       ├── __init__.py
│       ├── utils.py            # Configuración del WebDriver
│       ├── test_login.py       # Pruebas de inicio de sesión
│       ├── test_inventory.py   # Pruebas del inventario
│       └── test_cart.py        # Pruebas del carrito de compras
├── assets/
│   └── style.css               # Estilos para el reporte HTML
├── reporte.html                # Reporte generado tras la ejecución
└── README.md
```
