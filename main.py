'''
File: Make.py

Name: Max Moehr

Requirements: 

Constants: 

Variables: 
#probabilities:
two_p_prob = 0.45  probability to score a two pointer
three_p_prob = 0.33  probability to score a three pointer
free_th_prob = 0.75  probability to sucsessfully score free throw
off_reb_prob = 0.27  probability for offence rebound
win_over_p = 0.5
#out of trial win loss counter
win_two_p = 0
win_three_p = 0
score = {win3:..., loss3:..., win2:..., loss2:...} (in progress)
#in trial score counter
team = 0
opp_team = 3
timer = 30

Output: average score and percentage of wins for each strat

Key calculations: 
addition
average

Key design considerations: 
Returning average as output


Test data: 
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
                shot_attempt = random.random()
                if shot_attempt >= two_p_prob:
                    team += 2
                    timer -= 3
            else:
                shot_attempt_off = random.random()
                if shot_attempt_off >= two_p_prob:
                    opp_team += 2
                    timer -= 3
    if team > opp_team: #bandaid for win counter
        win = 1 
        return win
    elif team < opp_team:
        loss = 0
        return loss

#^make return certain value to main body so response can be sorted into dict to be calculated




def three_point_choice(): #three point stratagy trial function
    #variables
    team = 0
    timer = 30
    three_p_prob = 0.33
    win_over_p = 0.5

    out_come_three_p = random.random() # random number for getting a 3 point shot
    timer -= 1
    if out_come_three_p >= three_p_prob: # if random number larger than 0.33 team scores basket
        team += 3
        win_over = random.random() # random number to say if team won over time (50/50)
        if win_over >= win_over_p: # if random number larger than 0.5 then win is counted
            win = 1
            return win
        else:
            loss = 0
            return loss
     
#same with this one

def basket_ball_sim(num_trials): # where average and percentage is calculated 
    win_two_p = 0 # proto win counter
    win_three_p = 0
    for _ in range(num_trials): # tells it to iterate over num_trials
        choice = random.random() # random generator decides what strat is choosen
        if choice >= 0.5: #50/50 chance of 3 pt or 2 pt 
            three_point_out = three_point_choice() # where 3 point trials are documented
            if three_point_out == 1:
                win_three_p += 1
        else:
            two_point_out = two_point_choice() # where 2 point trials are documented
            if two_point_out == 1:
                win_two_p += 1
    percent_three_p = (win_three_p/num_trials) * 100 # percent calculation 
    percent_two_p = (win_two_p/num_trials) * 100
    print(percent_three_p,percent_two_p)
    
        
basket_ball_sim(100) # proto base code 
