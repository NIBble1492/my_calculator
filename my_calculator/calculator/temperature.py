import math

def celsius_to_fahrenheit(celsius):
    fahrenheit= round(float(celsius) * 1.8 + 32, 2)

    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((float(fahrenheit) - 32) / 1.8, 2)
    return  celsius
        