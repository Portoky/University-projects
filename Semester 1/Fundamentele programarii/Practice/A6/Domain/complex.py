def create_complex_number(a : int, b : int):
    '''
    Creates a dict representation of a complex number: a+bi
    :param a: integer, real part
    :param b: integer, imaginary part
    :return: dictionary representation
    '''
    return {"real": a, "imaginary": b}

def get_real_part(z : dict):
    return z["real"]

def get_imaginary_part(z : dict):
    return z["imaginary"]

def set_real_part(z : dict, value: int):
    z["real"] = value

def set_imaginary_part(z : dict, value : int):
    z["imaginary"] = value

def complex_to_string(z : dict):
    '''
    Forms a string in a+bi form
    :param z: dict representing complex number
    :return: string containging a+bi
    '''
    s = ""
    if get_real_part(z) < 0:
        s += str(get_real_part(z))
    elif get_real_part(z) > 0:
        s += str(get_real_part(z))
    if get_imaginary_part(z) < 0:
        s += str(get_imaginary_part(z)) + "i"
    elif get_imaginary_part(z) > 0:
        s += "+" + str(get_imaginary_part(z)) + "i"
    if get_real_part(z) == 0 and get_imaginary_part(z) == 0:
        s = "0"
    return s
