from random import choices  #homework dice.py
ntrials = 10000
player1wins = 0
ndice1 = 3           #Number of dice Player 1 rolls
ndice2 = 2                 #Number of dice Player 2 rolls
for i in range(ntrials) :
    dice2 = choices(range(1 , 7) , k=ndice2)        #Dice 2 (Player 2)
    if dice2[0] == dice2[1]:                         #Condition if two dice are equal for Player 2
        continue
    dice1 = choices(range(1 , 7) , k=ndice1)        #Dice 1(Player 1)
    dice1.sort(reverse=True)                      #Organize the dice so the highest number is the first
    if dice1[0] + dice1[1] > dice2[0] + dice2[1]:             #If the total sum of Player 1's 2 highest numbers is higher than the player 2 dice
        player1wins += 1                       #Player 1 wins
print("Ratio=", player1wins/ntrials)

# After running the simulation, we find that the ratio is around 2 or 3% above the 50% of fairness
# For this reason, we can say the game is not too fair