#######-INTRODUCTION-########
# This is the first Python program starting with a stucture to develop into a product
# the Main sections are
#
# 1.PACKAGES Section
# 2.FUNCTIONS Section
# 3.WELCOME STATEMENTS and Menu selection Section: The Menu is listed in this section and control moves to the Main program
# 4.MAIN Section 
# 

#######-END OF INTRODUCTION-########

######### URLS being used#######

# http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-1/

######## END OF URL REFERENCES

#############################################- 1. PACKAGES- ##################################
import time
############################################# - End of Packages - ##################################




######################################################## - 2.FUNCTIONS-##############################################
def sentiment(pwords,nwords):
    if pwords>nwords:
        print "The Sentence is  " + str((pwords/nwords)*100)+ "% positive Sentence"
    else:
        print "The Sentence is  " + str((nwords/pwords)*100)+ "% negative Sentence"

def checkwords(inputlist):
    print "Inside the checkwords func"
    positive_words =['awesome','good','nice','super','fun']
    negative_words = ['awful','lame','horrible','bad']
    emotional_words = positive_words+negative_words
    
    pwords=0
    nwords=0
    # Need to count multiple instances of the same words and also the number of unique words for both positive and negative
    # The current logic is only doing a count of unique instances of pwords and nwords, which is not correct,
    # because a sentence could have used same positive words multiple times
    # also find out how to take words from a txt file that was we can maintain lists of positive and negative words

    for words in inputlist:
            if words in positive_words:
                print "The Positive words are " + words
                pwords = pwords +1
            if words in negative_words:
                print "The Negative words are " + words
                nwords = nwords +1
    
    print "The number of Positive words are " + str(pwords)
    print "The number of Negative words are " + str(nwords)
  
    return(pwords, nwords)
    print "Exiting the checkwords func"
    # the function should return the number of positive words and number of negative words in the sentence
# End of Function

def splittingwords(sen):
    print "Inside the splittingwords func"
    print "Printing the sentence from inside func " +'\n' +sen
    print str(len(sen))
    splitwords = sen.split()
    #print type(splitwords)
    print "The total character count of the sentences is " + str(len(sen))
    print "The word count in the sentence is " + str(len(splitwords))
    print "Exiting the splittingwords func"
    return splitwords
# End of Function
    
def mynames(inputname):
    if inputname in ("Sarada" , "sarada", "Valli", "valli", "SARADA"):
        #print "Sarada check"
        return "Dear Darling....."
    if inputname in ("Mrini", "Vaishu", "Mrinalini", "Vaishnavi", "VAISHNAVI"):
        #print "Mrini Check"
        return "Dear Bangaram....."
    if inputname in ("Anish", "Tanmay", "Anish Tanmay", "anish", "ANISH"):
        #print "Anish Check"
        return "Dear Anish...."
    else :
        return inputname
# End of Function
     
def mywhile():
    print '\n' + "Inside While loop function" +'\n'
    n = 5
    while n > 0:
        print n
        n = n-1
    print 'Blastoff!'
# End of Function

def rcomputepay(x,y):
    if x <=40 :
        return x*y
    else :
        return y*40 + (y*1.5 *(x-40))
# End of Function

def raddition(x,y):
    #print "This is Addition"
    return x+y
# End of Function

def rsubstraction(x,y):
    #print "This is Substraction"
    return x - y
# End of Function

def rmultiply(x,y):
    #print "This is Multiplication"
    return x * y
# End of Function

def rdivide(x,y):
    #print "This is Division"
    return x / y
# End of Function

def basicmath(num1, num2):
    try:
            print '\n' + "What you want to do with the two numbers ? Please Select " +'\n'+"1.Addition" +'\n'+"2.Substraction" +'\n'+"3.Multiplication" +'\n'+"4.Division"+'\n'
            uinput = int(raw_input("Please Make a selection : "))
            if uinput ==  1:
                print "Very Well you choose Addition " 
                total = raddition(num1,num2)
                #print "After total"
                print "Sum of : " + str(num1) + " and " + str(num2) + " is " + str(total)
                return total
            if uinput ==  2:
                print "Very Well you choose Substraction "
                total = rsubstraction(num1,num2)
                print "Difference between : " + str(num1) + " and " + str(num2) + " is " + str(total)
                return total
            if uinput ==  3:
                print "Very Well you choose Multiplication"
                total = rmultiply(num1,num2)
                print "Multiplying " + str(num1) + " and " + str(num2) + " gives " + str(total)
            if uinput ==  4:
                print "Very Well you choose Division"
                total = rdivide(num1,num2)
                print "Dividing " + str(num1) + " and " + str(num2) + " gives " + str(total)
                
    except:
            print "If you want to learn basic maths please enter numbers between 1 to 4 only"
# End of Function

######################################################## - this is END OF FUNCTIONS SECTIONS--#####################################################################





############################## - 3. WELCOME STATEMENTS- #######################
print "Hello, Welcome to Python Program created by Ravi..., please enter your name"
xname = raw_input("What is your Name : ")
xname = mynames(xname)
print '\n'+"Hello " + xname + ", Welcome to Python Program, Today is " + time.strftime("%x")
print '\n'+ xname + ", Today you can choose From following options ..." +'\n'
print "Menu"+'\n'+"1.Calculate Pay" +'\n'+"2.Open and read a file"+'\n'+"3.Basic Math"+'\n'+"4.Using While and For Loops"+'\n'+"5.About Packages"
print "6.Reading and Writing to text files"+'\n'+"7.Working with R"+'\n'+"8.Working with Classes"+'\n'+"9.Working with MySQL DB"+'\n'+"10.Working with MySQL DB"+'\n'
##############################- END OF WELCOME STATEMENTS- #######################





######################################################## - 4. MAIN Section ###############################################################            
# if a selection other than a numeric is done, then pring please try numbers only
try:
    x = int(raw_input("Please Choose an option from 1 to 10 :"))
    
# if the selection is 1 then execute the following code for pay calculation
    if x == 1 :
        # the input is in string , convert it into float
        print '\n'+ xname +" Your Selection is : " + str(x)
        print '\n'+"This module calculates the pay of employee, you need to enter" + '\n' + "the hrs worked and rate of the employee" +'\n'
        hrs = float(raw_input("Please Enter the Hrs worked in a week : "))
        rate = float(raw_input("Please Enter the rate of pay : "))
        pay = rcomputepay(hrs,rate)
        print '\n' + "The Employee workded for " + str(hrs) + " hrs his total Pay @ the rate of $ " + str(rate) + " is $ " + str(pay)
        print '\n' + "If the emmployee works for more than 40 hrs in a week, the additional hrs are paid at the rate of 1.5 times the normal rate"
    if x == 2:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This is for opening, reading and priting a file "
        # Accept input to open a file
        # Compute the total word count and print
        # compute the highest frequency word
        # plot a graph of the top 5 high frequcny words
        # Compare the file with a another file which has categorized list of
        # words and return the Category to which the file belongs to
        # the logic is if it has 10% of the words in the input file has a match in the category file,
        #then the input file belongs to that particular category
    if x == 3:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "Welcome to Basic Math"
        print "Here you can practice basic maths on two numbers between 0 and 10"
        num1 = float(raw_input("First Number , Please enter a number from 0 to 10 : "))
        num2 = float(raw_input("Second Number, Please enter a number from 0 to 10 : "))
        rvalue=basicmath(num1, num2)
        #print rvalue
    if x == 4:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "Learning objectives include learning about while loops, for loops"
        mywhile()
    if x == 5:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module is to learn about importing and creating packages and using functions in the packages"
    if x == 6:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module opens a web page and reads the text and converts to a txt file and continues from Selection 2"
        print "1st we will learn how to read a short sentence and break it into individual words, for this lets call the function smallsentence"
        receivedstr = raw_input("Please enter a sentence max with 20 words... ")
        print "You Entered : " + receivedstr +'\n'
        splitstr=splittingwords(receivedstr)
        print '\n'+ "This is after returning from function "
        pwords, nwords=checkwords(splitstr)
        
        print '\n'+ "This is after Exiting from function "
        print "The number of Positive words are " + str(pwords)
        print "The number of Negative words are " + str(nwords)

        sentiment(pwords, nwords)
        
    if x == 7:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module involves integrating with Web, displaying Menu options to run Python programs from Web Server, accepts input and displays to Web"
    if x == 8:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module is for classes"
    if x == 9:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module Working with MySQL DB"
    if x == 10:
        print '\n'+ xname +" Your Selection is : " + str(x)
        print "This module Working with MySQL DB"
    if x > 10:
        print "Dear " + xname + " thanks for testing me...."+ '\n'+"We are still working on other options for now you can choose between 1 to 5 only..thank you have a nice day.."
except:
    print "Please enter numbers between 1 to 10 only"
    print "This error could be occuring due to an error in the splittingwords function"
######################################################## - END OF MAIN PROGRAM ##########################################################################     
