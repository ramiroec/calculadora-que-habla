# 🧮 Calculadora que Habla

**Autor:** Ramiro Estigarribia Canese

Bienvenido a **Calculadora que Habla**, una aplicación interactiva que realiza operaciones matemáticas básicas y comunica los resultados mediante síntesis de voz.

---

## 📋 Descripción

Esta calculadora soporta las siguientes operaciones:

- Suma
- Resta
- Multiplicación
- División
- Raíz cuadrada

¡Y además te habla! Después de seleccionar una operación, la aplicación te guiará con voz para completar el cálculo.

---

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/ramiroec/calculadora-que-habla.git
   ```
2. Entra en el directorio del proyecto:
    ```bash
   cd calculadora-que-habla    
   ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
   ```

## 🚀 Uso

1. Ejecuta la aplicación desde el archivo main.py:
    ```bash
    python main.py
    ```

2. Selecciona una de las operaciones disponibles en el menú interactivo.

3. Introduce los números para realizar la operación seleccionada.

4. ¡Escucha el resultado! La calculadora te dirá el resultado por voz.

## 📂 Estructura del Proyecto

```bash
calculator-que-habla/
│
├── calculator/
│   ├── operations.py   # Módulo que contiene las operaciones matemáticas
│   └── voice.py        # Módulo que maneja la síntesis de voz
│
├── main.py             # Archivo principal para interactuar con el usuario
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

## 💻 Requisitos

Python 3.x
Biblioteca pyttsx3 para la síntesis de voz (incluida en requirements.txt)

## 🗣️ Funcionalidad de Voz
La calculadora utiliza el paquete pyttsx3 para convertir texto en voz, haciendo la experiencia más interactiva. Si tienes algún problema con la síntesis de voz, asegúrate de que pyttsx3 esté correctamente instalado y funcionando en tu sistema.

## 📜 Licencia
<p>Este proyecto se encuentra bajo la licencia MIT.</p>


## 🤝 Contribuciones
<p>Si deseas contribuir a este proyecto, por favor, crea un pull request con tus cambios.</p>

## 🌟 Créditos
Código escrito con café ☕ y algo de paciencia por Ramiro Estigarribia Canese.

