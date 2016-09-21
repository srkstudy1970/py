##### To Import Packages########
import math
import os
import random


##### End of Packages#########

##### Welcom Message#########
print "Welcome to Ravi's Rock Paper Scissors Lizzard Spock (rpsls) program"
##### End of Welcome Messages #########

def name_to_num(name):
    if name == "rock":
        #print "You Choose rock"
        t = 0
    elif name == "paper":
        #print "You Choose paper"
        t = 1 
    elif name == "scissors":
        #print "You Choose scissors"
        t = 2
    elif name == "lizard":
        #print "You Choose lizard"
        t = 3
    elif name == "spock":
        #print "You Choose spock"
        t = 4
    else:
        t = 5
        print "Your typed " + name + " Please Type correctly"
    return t

def num_to_name():
    comp_number=random.randrange(0,4)
    #print str(num)
    if comp_number == 0:
        #print "Computer Choose rock"
        name = "rock"
    elif comp_number == 1:
        #print "Computer Choose paper"
        name = "paper"
    elif comp_number == 2:
        #print "Computer Choose scissors"
        name = "scissors"
    elif comp_number == 3:
        #print "Computer Choose lizard"
        name = "lizard"
    elif comp_number == 4:
        #print "Computer Choose spock"
        name = "spock"
    else:
        name = "Wrong"
        print "Computer Choose " + str(num)+ " this is Wrong, Computer lose"
    return name, comp_number

def rpsls(choice):
    #print "inside rpsls"
   #player_choice=str(raw_input("Please Type One of the following  Rock, Paper, Scissors, Lizard, Spock"+'\n'))
    player_choice=choice
    #print str(player_choice)
    player_number = name_to_num(player_choice)
    #print str(player_number)
    name, comp_number =num_to_name()
    #print "You Choose "+str(player_choice)+" which is  "+ str(player_number)
    #print "Computer Choose " + name + " which is "+str(comp_number)
    diff = (player_number-comp_number)%5
    #print str(diff)
    if diff == 0:
        print "You Choose "+str(player_choice)+" which is "+ str(player_number)
        print "Computer Choose " + name + " which is "+str(comp_number)
        print "Both Choose Same No Winner"+'\n'
    elif diff == 1 or diff == 2:
        print "You Choose "+str(player_choice)+" which is "+ str(player_number)
        print "Computer Choose " + name + " which is "+str(comp_number)
        print "YOU WIN COMPUTER LOSE"+'\n'
    elif diff == 3 or diff == 4:
        print "You Choose "+str(player_choice)+" which is "+ str(player_number)
        print "Computer Choose " + name + " which is "+str(comp_number)
        print "YOU LOSE COMPUTER WIN"+'\n'
        
    
   
#rpsls(raw_input("Please Type One of the following  rock, paper, scissors, lizard, spock   : "))
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
