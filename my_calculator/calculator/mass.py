import math

def mass_calculator(before_type, before_num, after_type):
    if before_type == "gram":
        before_num = float(before_num)
    elif before_type == "kilogram":
        before_num = float(before_num) * 1000
    elif before_type == "ounce":
        before_num = float(before_num) * 28.349523125
    elif before_type == "pound":
        before_num = float(before_num) * 453.59237

    if after_type == "gram":
        return round(before_num, 2)
    elif after_type == "kilogram":
        return round(before_num / 1000, 2)
    elif after_type == "ounce":
        return round(before_num / 28.349523125, 2)
    elif after_type == "pound":
        return round(before_num / 453.59237, 2)

