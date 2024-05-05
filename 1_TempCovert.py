import tkinter as tk
from tkinter import ttk

def validate_temperature_input(text):
    if text.isdigit() or (text == "" and len(temperature_entry.get()) == 0):
        return True
    else:
        return False

def convert_temperature():
    try:
        temperature = float(temperature_entry.get())
        unit = unit_combobox.get().lower()

        if unit == "celsius":
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.15
            result_label.config(text=f"{temperature}° Celsius is equal to: \n {fahrenheit:.2f}° Fahrenheit \n {kelvin:.2f} Kelvin.")
        elif unit == "fahrenheit":
            celsius = (temperature - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(text=f"{temperature}° Fahrenheit is equal to: \n {celsius:.2f}° Celsius \n {kelvin:.2f} Kelvin.")
        elif unit == "kelvin":
            celsius = temperature - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{temperature} Kelvin is equal to: \n {celsius:.2f}° Celsius \n {fahrenheit:.2f}° Fahrenheit.")
        else:
            result_label.config(text="Please enter a valid unit (Celsius, Fahrenheit, Kelvin).")
    except ValueError:
        result_label.config(text="Please enter a valid temperature.")

def close(): 
    root.destroy()

root = tk.Tk()
root.title("Temperature Converter")

temperature_label = tk.Label(root, text="Enter temperature:")
temperature_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
validate_input = root.register(validate_temperature_input)  # Register the validation function
temperature_entry = tk.Entry(root, validate="key", validatecommand=(validate_input, "%S"))
temperature_entry.grid(row=0, column=1, padx=10, pady=5)

unit_label = tk.Label(root, text="Select unit:")
unit_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
unit_combobox.grid(row=1, column=1, padx=10, pady=5)
unit_combobox.set("Celsius")  # Set default unit to Celsius
unit_combobox.config(foreground="gray")  # Set text color to gray

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

exit_button = tk.Button(root, text="Exit", command=close)
exit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()