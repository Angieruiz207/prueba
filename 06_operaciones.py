# ***OPERACIONES ARITMETICAS*******
# SUMA +, RESTA -, MULTI -, DIVI/, DIV ENTERA //, Jerarquia: (),**,
#RESIDUO O MÓDULO %, POTENCIA **
number = int(input('Digite un número:'))
print(f'La suma con 2 es:{number + 2}')
print(f'La resta con 2 es:{number - 2}')
print(f'La multiplicación con 2 es:{number * 2}')
print(f'La división con 2 es:{number / 2}')
print(f'La división entera con 2 es:{number // 2}')
print(f'El residuo con 2 es:{number % 2}')
print(f'La potencia con 2 es:{number ** 2}')

# OPERACIONES DE ASIGNACIÓN
contador = 1
print(f'antes de += {contador}')
contador += 1  ## contador = contador + 1 ## Operador de asignación
print(f'despues de += {contador}')
contador = 9
contador -= 1  ## Operador de asignació decremental
number += 1
print(f'Al usar el operador incremental += el resultado es:{number}')
number -= 1
print(f'Al usar el operador decremental -= el resultado es:{number}')
number *= 2
print(f'Al usar el operador *=  el resultado es:{number}')
number /= 2
print(f'Al usar el operador /= el resultado es:{number}')
number //= 2
print(f'Al usar el operador //= el resultado es:{number}')
number %= 3
print(f'Al usar el operador %= el resultado es:{number}')
number **= 2
print(f'Al usar el operador **= el resultado es:{number}')
