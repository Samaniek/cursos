import random
from typing import Counter

options = ('piedra', 'papel', 'tijera')

computadora_wins = 0
user_wins = 0
rondas = 1

while True:
  
  print('*' * 10)
  print('ronda', rondas)
  print('*' * 10)

  print(f'computadora_wins: {computadora_wins}')
  print(f'user_wins: {user_wins}')

  user_option = input('piedra, papel o tijera =>')
  user_option = user_option.lower()

  rondas +=1
  
  if not user_option in options:
    print('esa opcion no es valida')
    continue
    
  computadora_option = random.choice(options)
  
  
  print('user_option =>', user_option)
  print('computadora_option =>', computadora_option)
  
  if user_option == computadora_option:
    print('empate')
  
  elif user_option == 'piedra':
    if computadora_option == 'tijera':
      print('piedra gana a tijera')
      print('user a ganado!')
      user_wins += 1
      
    else:
      print('papel gana a piedra')
      print('computadora gano!')
      computadora_wins += 1
  
  elif user_option == 'papel':
    if computadora_option == 'piedra':
      print('papel gana a piedra')
      print('user a ganado!')
      user_wins += 1
      
    else:
      print('tijera gana a papel')
      print('computadora gano!')
      computadora_wins += 1
      
  elif user_option == 'tijera':
    if computadora_option == 'papel':
      print('tijera gana a papel')
      print('user a ganado!')
      user_wins += 1
      
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computadora_wins += 1

  if computadora_wins == 2:
    print('El ganador es la computadora')
    break

  if user_wins == 2:
    print('El ganador es el usuario')
    break
  
  
  '''
  number = int(input("Ingrese un numero => "))
  result =  number % 2
  if (result == 0):
      print("El número es par")
  else:
      print("El número es impar")
  '''