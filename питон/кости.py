import random
playerOneName = input('Введите имя 1го игрока')
playerTwoName = input('Введите имя 2го игрока')
diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]
playerOneScore = 0
playerTwoScore = 0
def throwDice():
   for i in range(5):
       random.shuffle(diceOne)
       random.shuffle(diceTwo)
   return diceOne[0] + diceTwo[0]
for i in range(3):
   result = throwDice()
   playerOneScore += result
   print('Игрок ', playerOneName, 'выбосил:', result)
   print("Сумма очков у игрока", playerOneName, ":", playerOneScore)
   nextTurn = input('Чтобы сделать следующий бросок нажмите кнопку Enter \n')

if playerOneScore > playerTwoScore: