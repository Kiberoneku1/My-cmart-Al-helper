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
  def