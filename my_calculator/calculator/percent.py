import math

def total_to_value(total_value, proportion):
    ans = float(total_value) * (int(proportion) / 100)
    return ans

def total_to_proportion(total_value, some_value):
    ans = round((float(some_value) / float(total_value)) * 100, 2)
    return str(ans) + " %"
def standard_to_value(standard_value, proportion, inc_dec):
    if inc_dec == "up":
        ans = float(standard_value) + (float(standard_value) * (int(proportion) / 100))
        return ans
    else:
        ans = float(standard_value) - (float(standard_value) * (int(proportion) / 100))
        return ans

def standard_to_proportion(standard_value, change_value):
    ans = 100 - round((float(change_value) / float(standard_value)) * 100, 2)
    if ans >= 0:
        ans = abs(ans)
        return str(ans) + " % 감소"
    else:
        ans = abs(ans)
        return str(ans) + " % 증가"

