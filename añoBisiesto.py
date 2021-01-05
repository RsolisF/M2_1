def bisiesto(anio):
    if anio%400==0:
        return True
    else:
        if anio%4==0 and anio%100!=0:
            return True
        else:
            return False

