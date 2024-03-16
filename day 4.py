import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player = int(input( "What do you choose ?\n1 for rock\n2 for paper\n3 for scissors "))
if player == 1:
  print(rock)
elif player == 2:
  print(paper)
else:
  print(scissors)

pc = random.randint(1,3)

if pc == 1:
  print(rock)
elif pc == 2:
  print(paper)
else:
  print(scissors)

if player == pc:
  print("Its a tie, try again")
elif player == 1 and pc == 2:
  print("You lose")
elif player == 2 and pc == 1:
  print("You win")
elif player == 2 and pc == 3:
  print("You lose")
elif player == 3 and pc == 2:
  print("You win")
