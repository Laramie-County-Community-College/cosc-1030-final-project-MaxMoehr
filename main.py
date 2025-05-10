'''
File: Make.py

Name: Max Moehr

Requirements: 
-Monte Carlo Simulation
-Parameters : use variables to store parameters
-Accurately represent game logic (three point and foul scenarioes)
-Display results : percentage of wins for each stratagy, ave number of points scored in each scenarieo


Constants: probabilities, win loss

Variables: 
#probabilities:
two_p_prob = 0.45  probability to score a two pointer
three_p_prob = 0.33  probability to score a three pointer
free_th_prob = 0.75  probability to sucsessfully score free throw
off_reb_prob = 0.27  probability for offence rebound
win_over_p = 0.5
#out of trial win loss counter
three_point_amount = how many games won by three strat
two_point_amount = how many games won by two point foul strat
score_saver_two = where score for each two point match are kept
score_saver_three = score for three point match is stored
win_three_p = how many times three point won
win_two_p = how many times two point won
#in trial score counter
team = 0
opp_team = 3
timer = 30
loss = 0
win = 1

Output: average score and percentage of wins for each strat

Key calculations: 
addition
average

Key design considerations: 
Returning average and percentage as output


Test data: 
output: 'enter number of trials:'
user input: 200
output:
When in the last thirty seconds of a game, three points down it was found:
 The percentage chance of winning with a three point stratagy: 
  16.0%
 The percentage chance of winning with a two point and foul stratagy:  
  23.5%
 The average points scored using a three point stratagy: 
  1.9
 The average points scored using a two point and foul stratagy: 
  8.4

'''
import random

def two_point_choice(): #two point strat function
    #variables
    two_p_prob = 0.45
    free_th_prob = 0.75
    team = 0
    opp_team = 3
    timer = 30
    off_reb_prob = 0.27
    win = 1
    loss = 0

    out_come_two_p = random.random() #random number 
    timer -= 1 #time to take shot
    if out_come_two_p >= two_p_prob: #random number to decide if two point shot made it in basket
        team += 2 #points won
        timer -= 3 #time it takes to foul
        free_throw1 = random.random() #free throws generated
        free_throw2 = random.random()
        if free_throw1 >= free_th_prob: #freethrows made it (+1pt or +2pt) or not (no points)
            opp_team += 1
        if free_throw2 >= free_th_prob:
            opp_team += 1
        while timer > 0: #countdown continues after free throw is made (fixed?)
            off_reb = random.random() #rebound random number generator
            if off_reb >= off_reb_prob: # decides if we get ball or opponent gets ball
                shot_attempt = random.random() #if our team misses or not
                if shot_attempt >= two_p_prob:
                    team += 2
                    timer -= 3
            else:
                shot_attempt_off = random.random() #weather or not opposing team misses
                if shot_attempt_off >= two_p_prob:
                    opp_team += 2
                    timer -= 3
    
    if team > opp_team: # sends wins and losses and score to body
        win = 1 
        return win, team
    
    elif team < opp_team:
        loss = 0
        return loss, team
    else:
        overtime = random.random()
        if overtime > 0.5:
            return win, team
        else:
            return loss, team



def three_point_choice(): #three point stratagy trial function
    #variables
    team = 0
    timer = 30
    three_p_prob = 0.33
    win_over_p = 0.5
    win = 1
    loss = 0

    out_come_three_p = random.random() # random number for getting a 3 point shot
    timer -= 1
    if out_come_three_p >= three_p_prob: # if random number larger than 0.33 team scores basket
        team += 3
        win_over = random.random() # random number to say if team won over time (50/50)
        if win_over >= win_over_p: # if random number larger than 0.5 then win is counted
            win = 1
            return win, team
        else:
            loss = 0
            return loss, team
    else:
        return loss, team
     
#asks user for trial number
num_trials = int(input("enter number of trials: "))

#variables, lists
three_point_amount = 0
two_point_amount = 0
score_saver_two = []
score_saver_three = []
win_three_p = 0
win_two_p = 0

for _ in range(num_trials): # tells it to iterate over num_trials
    choice = random.random() # random generator decides what strat is choosen
    if choice >= 0.5: #50/50 chance of 3 pt or 2 pt 
        three_point_out, score_three = three_point_choice() #unpacking win or loss and score
        three_point_amount += 1 #counts how many times three strat was used
        if score_three != 0:
            score_saver_three.append(score_three) #removes zeros
        if three_point_out == 1:
                win_three_p += 1 #counts how many times three point strat won
    else:
        two_point_out, score_two = two_point_choice() # where 2 point trials are documented
        two_point_amount += 1 #count of two point foul strat games
        if score_two != 0: #removes zeros
            score_saver_two.append(score_two)
        if two_point_out == 1:
            win_two_p += 1 #counts how many times two point foul strat won



 #sums score lists
sum_three = sum(score_saver_three)
sum_two = sum(score_saver_two)
 #averages score to points per game
ave_score_two = sum_two / two_point_amount
ave_score_three = sum_three / three_point_amount
 #percent calculation for each strat
percent_three_p = (win_three_p/num_trials) * 100 
percent_two_p = (win_two_p/num_trials) * 100

 #gives to user as output
print(f'When in the last thirty seconds of a game, three points down it was found:')
print(f' The percentage chance of winning with a three point stratagy: \n  {percent_three_p:.1f}%')
print(f' The percentage chance of winning with a two point and foul stratagy:  \n  {percent_two_p:.1f}%')
print(f' The average points scored using a three point stratagy: \n  {ave_score_three:.1f}')
print(f' The average points scored using a two point and foul stratagy: \n  {ave_score_two:.1f}')