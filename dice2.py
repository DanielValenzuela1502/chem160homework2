from random import choices #homework dice2.py
ntrials = 10000
player1wins = 0
ndice1 = 3      #Number of dice Player 1 rolls
ndice2 = 2      #Number of dice Player 2 rolls
for i in range(ntrials):
    dice2 = choices(range(1 , 7) , k=ndice2)        #Dice 2 (Player 2)
    if dice2[0] == dice2[1]:                  #Condition if two dice are equal for Player 2
        continue
    dice1 = choices(range(1 , 7) , k=ndice1)    #Dice 1(Player 1)
    dice1.sort(reverse=True)                     #Organize the dice so the highest number is the first
    if dice1[1] == dice1[2] == 2 or dice1[0] == dice1[1] == 2 or dice1[0] == dice1[1] == dice1[2]==2:  #If there are two or more 2's
        player1wins=player1wins+0      #No wins if there are two or more 2's given by above conditional
        continue
    if dice1[0] + dice1[1] > dice2[0]+dice2[1]:  #If the total of the highest 2 dice of Player 1 are higher than the player 2 sum dice
        player1wins += 1      #Player 1 wins

print("Ratio=", player1wins/ntrials)


# After running the simulation, we find that the ratio is slightly smaller than the last game rules
# Because the ratio is much closer to 50%  than the last game, we can say this added rule improves fairness.