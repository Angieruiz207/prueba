number = int(input('Digite un número:'))
#*****OPERACIONES RELACIONALES O DE COMPARACIÓN******
# True (1)/ False (0)
print(number > 3)  # pregunta si number es mayor que 3
print(number >= 3)  # pregunta si number es mayor o igual a 3
print(number < 3)  # pregunta si number es menor que 3
print(number <= 3)  # pregunta si number es menor o igual a 3
print(number == 3)  #pregunta si number es igual a 3
print(number != 3)  # si number es diferente a 3

# *****OPERACIONES LÓGICAS*******
# True (1)/ False (0)
#Basicas
print('Operaciones Lógicas')
print('Conjunción')
#conjunción (AND &) Si un resultado es falso el resultado siempre es Falso
print(False and False)
print(False & False & False)
print((number >= 3) and True)
print((number >= 3) and False)
print('Disyunsión')
#Disyunción (OR Siempre que exista un valor verdadero el resultado sera verdadero
print (False | True)
print(number <= 3 |number >= 10)
print(number <= 3 or number >= 10)

# pregunta si number es mayor o igual a 3

#Negación (NOT ~)
print ('Negación')
print (not (True))
print(not(number <= 3 |number >= 10))

# Or exclusiva (^)
print ('Or exclusiva')
print (False ^ False)
print (False ^ True)
print (True ^ False)
print (True ^ True)

## ***Operaciones de Pertenencia (in)****
#in
print ('Operadores Pertenencia')
nombre = ' Cesar Quintero'
print ('Q' in nombre)
print ('Z' in nombre)
