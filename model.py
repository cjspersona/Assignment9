class TemperatureModel:
    def fahrenheit_to_celsius(self, fahrenheit_text):
        try:
            fahrenheit = float(fahrenheit_text)
            celsius = (fahrenheit - 32) * 5 / 9
            return f"{celsius:.2f} °C"
        except ValueError:
            return "Please enter a valid number."