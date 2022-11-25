

def notation_calculator(before_type, before_num, after_type):
    if before_type == "binary":
        before_num = int(before_num, base=2)
    elif before_type == "octal":
        before_num = int(before_num, base=8)
    elif before_type == "decimal":
        before_num = int(before_num)
    elif before_type == "hexadecimal":
        before_num = int(before_num, base=16)

    if after_type == "binary":
        return format(before_num, 'b')
    elif after_type == "octal":
        return format(before_num, 'o')
    elif after_type == "decimal":
        return int(before_num)
    elif after_type == "hexadecimal":
        return format(before_num, 'x')
   