import random
choices = ['камень', 'ножницы', 'бумага']
def get_winner(player, computer):
   if player == computer:
       result = "Ничья!"
   elif (player == "камень" and computer == "ножницы") or \
        (player == "ножницы" and computer == "бумага") or \
        (player == "бумага" and computer == "камень"):
       result = "Вы выиграли!"
   else:
       result = "Вы проиграли!"
   return result
def playGame():
   print('Игра "Камень-Ножницы-Бумага!" ')
   print('Для входа в игру нажмите "Enter"')
   while True:
       player = input('ваш выбор').lower()
       if player =='выход':
           print('Спасибо за игру')
           break
       if player not in choices:
           print('Неверный ввод! Попробуйте: камень, ножницы, бумага')
           continue
       computer = random.choice(choices)
       print(f'Компьтер выбрал {computer}!')
       result = get_winner(player, computer)
       print(result)
playGame()
