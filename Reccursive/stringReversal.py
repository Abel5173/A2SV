def stringRevesrsal(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + stringRevesrsal(string[:-1])