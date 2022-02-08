import random

def getWord() :
  from wordfile import words
  word = random.choice (words)
  return word 

while True:
  word = getWord()
  if len(word) ==3 :
    break
  elif 
 


    

word = list(word)
print('Please guess your word')
print("_ "*len(word))

answer = "_"*len(word)
answer =  list(answer)

turn = 0
while True :
  if answer == word :
    print("YOU WON !")
    break
  guess = input("Enter your guess - ").lower()
  turn=turn + 1
  if guess in word : 
    for i in range(len(word)) :
      if word[i]==guess :
        answer[i]=guess 
        print('CORRECT GUESS')
        print(" ".join(answer))
  else :
    print("WRONG GUESS TRY AGAIN")