import random
import os
from playsound import playsound
playsound ('D:\\Usman\\PYTHON\\PROJECTS\\Rock Paper And Scissor Game\\house.mp3')
def game(comp,you):
    if comp == you:
        return None
    elif(comp=='r'):
        if(you=='p'):
            return True
        elif(you=='s'):
          return False
    elif(comp== 's'):
        if(you == 'r'):
            return True
        elif(you == 'p'):
            return False
    elif(comp == 'p'):
        if(you == 's'):
            return True
        elif(you == 'r'):
           return False  
randNo = random.randint(1,3)
comp = print("Computer Turn: Rock(r) Paper(p) And Scissor(s) : ")
print("Computer Picked it Now!")
if(randNo == 1):
 comp = 'r'
elif(randNo==2):
 comp = 'p'
else:
 comp = 's'
you = input("Player Turn: Rock(r) Paper(p) And Scissor(s) : ")
print(f"Computer Choose : {comp}")
print(f"Player Choose : {you}")
result = game(comp,you)
if(result == None):
    print("The Game is a Tie")
    playsound ('D:\\Usman\\PYTHON\\PROJECTS\\Rock Paper And Scissor Game\\tie.mp3')
elif(result):
    print("You Win!")
    playsound ('D:\\Usman\\PYTHON\\PROJECTS\\Rock Paper And Scissor Game\\win.mp3')
else:
    print("You Lose!")
    playsound ('D:\\Usman\\PYTHON\\PROJECTS\\Rock Paper And Scissor Game\\lose.mp3')
