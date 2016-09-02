#######################- About this Program-##############
#print "This is for text analysis"
#print "Welcome to text analysis Module, "
#1. Packages
#2. Functions
#3. Welcome Menu
#3. Main 
#######################- END -About this Program-##############

#######################- Packages-##############
#print "Packages"
import time    

#######################- End of Packages-##############

#######################- Functions-##############

def printwords(x):
    """ 
        to print the names which are stored in the list
    """
    print "inside print words function"
    p=len(x)
    for a in range(0,p):
        print x[a]
    

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

def checkwords(inputlist):
    #print "Inside the checkwords func"
    positive_words =['awesome','good','nice','super','fun']
    negative_words = ['awful','lame','horrible','bad']
    emotional_words = positive_words+negative_words
    
    pwords=0
    nwords=0
    """
    # Need to count multiple instances of the same words and also the number of unique words for both positive and negative
    # The current logic is only doing a count of unique instances of pwords and nwords, which is not correct,
    # because a sentence could have used same positive words multiple times
    # also find out how to take words from a txt file that was we can maintain lists of positive and negative words
    """
    for words in inputlist:
            if words in positive_words:
                #print "The Positive words are " + words
                pwords = pwords +1
            if words in negative_words:
                #print "The Negative words are " + words
                nwords = nwords +1
    
    print "The number of Positive words are " + str(pwords)
    print "The number of Negative words are " + str(nwords)
    return(pwords, nwords)
    print "Exiting the checkwords func"
    # the function should return the number of positive words and number of negative words in the sentence
# End of Function


# sentiment
def sentiment(pwords,nwords):
    print "Inside sentiment function"
    print str(len(sen))
    print str(float(pwords)/len(sen))
    if pwords>nwords:
        print "The Sentence is  " + str((float(pwords)/len(sen))*100)+ " % positive"
    else:
        print "The Sentence is  " + str((float(nwords)/len(sen))*100)+ " % negative "

# End of Sentiment function

#print "Function mynames"
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

# Function reports

def reports():
    print "inside Function reports"
    x = 20
    y = 10
    z = 15
    # positive words =a
    a = 4
    # positive words =b
    b = 5
    # positive words = c
    c = 5
    print "Within in Reports Functions"
    print "A total of words in the Sentence are " + str(x)
    print "The number of stop words are : " + str(z)
    print "Total number of words in the sentence AFTER REMOVING STOP WORDS : " + str(y)
    print "The number of unique words are : " + str(a)
    print "The number of positive words are : " + str(b)
    print "The number of Negative words are : " + str(c)

# of Function


#######################- End of Functions-##############

#######################- Welcome Menu-##############
print "Hello, Welcome to Python Program for Text Analysis created by Ravi..., please enter your name"
xname = raw_input("What is your Name : ")
xname = mynames(xname)
print '\n'+"Hello " + xname + ", Welcome to Python Program, Today is " + time.strftime("%x")
print '\n'+ xname + ", Today you can choose From following options ..." +'\n'
print "Menu"+'\n'+"1.Simple Sentence Analysis" +'\n'+"2.File/Document Analysis"+'\n'+"3.Twitter Feed analysis"+'\n'+"4.Facebook feed Analysis"+'\n'+"5.Open"
print "6.Open"+'\n'+"7.Open"+'\n'+"8.Open"+'\n'+"9.Open"+'\n'+"10.Open"+'\n'

#######################- End of Welcomg Menu-##############

#######################- Main-##############
#print "Main"
try:
    x = int(raw_input("Please Choose an option from 1 to 10 :"))
    print type(x)
    
    if x == 1:
        print "Welcome to Sentence Analysis"
      
        sen =raw_input("Please Enter the text to analyze :" + '\n')
        print "The Sentence your entered is ..." +'\n' + sen + '\n'
        after_splitting=splittingwords(sen) # the splittingwords function will return a list
        #print type(after_splitting)
        print '\n'
        #print after_splitting
        """ 
        to print the names which are stored in the list
        """
        printwords(after_splitting) # printwords prints the words which are stored in the list, this is only for testing
        # to check words against a given list of p and n words
        pwords,nwords=checkwords(after_splitting) #checkwords function will take a list and check against p and n words and give a count
        
        sentiment(pwords,nwords)
        
        # to prepare a Summary report of the analysis
       
       
        # reports()

        
        #reports()
    if x == 2:
       print "Welcome to File/Document Analysis"
    if x == 3:
       print "Welcome to Twitter Feed Analysis"
    if x == 4:
        print "Welcome to Facebook Analysis"
except:
    print "Please eneter only a number between 1 and 4, now you need to run the program again, Its ok we will fix it"
#######################- End of Main-##############
