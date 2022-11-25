import math

def area_calculator(before_type, before_num, after_type):
    if before_type == "square_meter":
        before_num = float(before_num)
    elif before_type == "pyeong":
        before_num = float(before_num) * 3.3058
    elif before_type == "square_feet":
        before_num = float(before_num) / 10.764

    if after_type == "square_meter":
        return round(before_num, 2)
    elif after_type == "pyeong":
        return round(before_num/3.3058, 2)
    elif after_type == "square_feet":
        return round(before_num*10.764, 2)
    

