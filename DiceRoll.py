#DiceRoll.py
#Name:Juan V Mancilla Vargas
#Date: 2/25/2025
#Assignment: DiceRoll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    totaldices= dice1 + dice2

    rolls[totaldices - 2] = rolls[totaldices - 2] + 1
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 2
  for count in rolls:
    print(dice, ":", count)
    dice = dice + 1

if __name__ == '__main__':
  main()
