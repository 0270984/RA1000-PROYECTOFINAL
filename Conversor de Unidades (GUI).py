import tkinter as tk
from tkinter import ttk

# Funciones de conversión
def convert():
    try:
        input_value = float(entry_value.get())
        
        if selected_conversion.get() == "Metros a Kilómetros":
            result = input_value / 1000
        elif selected_conversion.get() == "Kilómetros a Metros":
            result = input_value * 1000
        elif selected_conversion.get() == "Libras a Kilogramos":
            result = input_value * 0.453592
        elif selected_conversion.get() == "Kilogramos a Libras":
            result = input_value / 0.453592
        elif selected_conversion.get() == "Celsius a Fahrenheit":
            result = (input_value * 9/5) + 32
        elif selected_conversion.get() == "Fahrenheit a Celsius":
            result = (input_value - 32) * 5/9
        else:
            result = "Selección no válida"
        
        label_result.config(text=f"Resultado: {result:.2f}")
    except ValueError:
        label_result.config(text="Por favor, ingrese un número válido")

# Configuración de la ventana principal
window = tk.Tk()
window.title("Conversor de Unidades")

# Label de instrucciones
label_instruction = tk.Label(window, text="Ingrese el valor y seleccione la conversión:")
label_instruction.pack(pady=10)

# Entrada de valor
entry_value = tk.Entry(window, width=20)
entry_value.pack(pady=5)

# Lista de opciones de conversión
conversion_options = [
    "Metros a Kilómetros",
    "Kilómetros a Metros",
    "Libras a Kilogramos",
    "Kilogramos a Libras",
    "Celsius a Fahrenheit",
    "Fahrenheit a Celsius"
]

selected_conversion = tk.StringVar(value=conversion_options[0])
conversion_menu = ttk.Combobox(window, textvariable=selected_conversion, values=conversion_options, state="readonly")
conversion_menu.pack(pady=5)

# Botón para convertir
button_convert = tk.Button(window, text="Convertir", command=convert)
button_convert.pack(pady=10)

# Label para mostrar el resultado
label_result = tk.Label(window, text="Resultado: ")
label_result.pack(pady=10)

# Iniciar la aplicación
window.mainloop()
