def main():
  import random

  dice_rolls = int(input("How many dice would you like to roll?\t"))
  dice_size = int(input("How many sides are the dices?\t"))
  dice_sum = 0

  for i in range(0, dice_size):
    roll = random.randint(1,dice_size)
    dice_sum += roll

    if roll == 1:
      print(f"You rolled a {roll}! Critical Fail")
    elif roll == dice_size:
      print(f"You rolled a {dice_size}! Critical Success") # The highest number a dice can roll is the same as the number of sides
    else:
      print(f"You rolled a {roll}")
  print(f'You rolled a total of {dice_sum}')

#Potential next steps
"""
    1. Add more inputs (like player or team name).
    2. Store each player's roll totals in separate arrays.
    3. Choose a dice-based game that you can fully simulate using python.
"""

if __name__== "__main__":
  main()

