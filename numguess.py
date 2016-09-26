import math
import random
def halfthenumber(n):
    n=n/2
    return n
    
humannum=float(raw_input("Please Enter a number between 0 and 100 "))
compguess = random.randrange(0,100)
guesscount=1

#print "The Entered number between (0 and 1000) is : " + str(humannum)
#print "The Current Guess is : " + str(compguess)

l="lower"
u= "upper"
try:
    while humannum != compguess:
        ans=raw_input("Computer Guess is " +str(compguess)+" is your number l=lower or h=higher or s=same : ")

        if ans == "l":
            #print "Computer guess is higher"
            p=round(compguess)-round(humannum)
            compguess= halfthenumber(p)
            print "The Current Computer Guess is : " +str(compguess)
            guesscount +=1
        elif ans == "h":
            #print "Computer guess is lower"
            p=round(humannum)+ round(compguess)
            compguess= halfthenumber(p)
            print "The Current Computer Guess is : " +str(compguess)
            guesscount +=1
        elif ans == "s":
            print "you are correct,then number is "+str(compguess)
            break
except:
        print "Please enter the following only l=lower or h=higher or s=same"
    
    
print '\n'+"Computer took " +str(guesscount)+ " iterations to guess your number"
