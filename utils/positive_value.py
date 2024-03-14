def is_positive_number(value):
    try:
        number_pos = float(value) 
    except ValueError:
        return False
    return number_pos > 0