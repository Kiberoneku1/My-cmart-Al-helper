board= [1,2,3,4,5,6,7,8,9]
def drawBoard(board):
   print('-'*13)
   for i in range (3):
       print('|', board[0+i*3], '|', board[1+i*3],'|', board[2+i*3] ,'|')
       print('-' * 13)
def takeInput(playerToken):
  valid = False
  while not valid:
     playerAnswer = input("Куда поставим " + playerToken+"? ")
     if not isValidInput(playerAnswer):
       continue
     playerAnswer = int(playerAnswer)
     if (playerAnswer >= 1 and playerAnswer <= 9):
        if(str(board[playerAnswer-1]) not in "XO"):
           board[playerAnswer-1] = playerToken
           valid = True
        else:
           print("Эта клетка уже занята!")
     else:
       print("Некорректный ввод. Введите число от 1 до 9.")
def isValidInput(playerAnswer):
 try:
   playerAnswer = int(playerAnswer)
   return True
 except:
   print("Некорректный ввод. Вы уверены, что ввели число?")
   return False
def checkWin(board):
   winCoords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
   for coord in winCoords:
       if board[coord[0]] == board[coord[1]] == board[coord[2]]:
           return board[coord[0]]
   return False
def main(board):
   counter = 0
   win = False
   while not win:
       drawBoard(board)
       if counter % 2 == 0:
           takeInput("X")
       else:
           takeInput("O")
       counter += 1
       if counter > 4:
           isWin = checkWin(board)
           if isWin:
               print (isWin, "выиграл!")
               win = True
               break
       if counter == 9:
           print ("Ничья!")
           break
   drawBoard(board)


# Запуск игры
if __name__ == "__main__":
    main(board)
