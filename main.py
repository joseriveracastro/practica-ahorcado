palabra = 'fresa'
fallos = 0
adivinar = []
for letra in range(len(palabra)):
    adivinar.append('- ')

palabra_con_espacios = []
for char in palabra:
  palabra_con_espacios.append(char)

print(palabra_con_espacios)

letras_usadas = [] 

while fallos < 7:
  if fallos == 0:
    print('________')
    print('!   |  !')
    print()
  elif fallos == 1:
    print('________')
    print('!   |  !')
    print('    o   ')
    print()
  elif fallos == 2:
    print('________')
    print('!   |  !')
    print('    o   ')
    print('    |   ')
    print()
  elif fallos == 3:
    print('________')
    print('!   |  !')
    print('    o   ')
    print('   \|   ')
    print()
  elif fallos == 4:
    print('________')
    print('!   |  !')
    print('    o   ')
    print('   \|/  ')
    print()
  elif fallos == 5:
    print('________')
    print('!   |  !')
    print('    o   ')
    print('   \|/  ')
    print('   /    ')
    print()
  elif fallos == 6:
    print('________')
    print('!   |  !')
    print('    o   ')
    print('   \|/  ')
    print('   / \\ ')
    print()
    print('Perdiste!!')
    break
    
  print(''.join(adivinar))
  print('letras_usadas: ', letras_usadas)
  print('Esta letra es',adivinar)
  print('Dime una letra:')
  tu_letra = input()

  if tu_letra in letras_usadas:
    print('Esa letra ya la colocaste...')
    print('Entra aqui')
  else:
    letras_usadas.append(tu_letra)
    hay_error = True
    for letra in range(len(palabra)):
        if tu_letra == palabra[letra]:
            adivinar[letra] = tu_letra
            hay_error = False
    if hay_error:
       fallos += 1
    print('Entramos aqui')
    print(palabra_con_espacios)
    print(adivinar)
    if palabra_con_espacios == adivinar:
       print(''.join(adivinar))
       print('Ganaste')
       break
  

    



  
   






