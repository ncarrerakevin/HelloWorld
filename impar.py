# .strip():
#
# Elimina cualquier espacio en blanco (espacios, saltos de línea) al principio y
# al final de la cadena que se obtuvo con input().
# Esto asegura que si el usuario accidentalmente coloca espacios o presiona Enter varias veces,
# esos espacios adicionales no afecten la entrada.

if __name__ == '__main__':

    n = int(input().strip())
    if n%2 != 0:
        print('Weird')
    else:
        if n >=2 and n<=5:
            print('Not Weird')
        elif n >=6 and n<=20:
            print('Weird')
        else:
            print('Not Weird')

