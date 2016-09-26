def charcount(s):
    numVowels = 0
    numCons = 0

    for char in s:
        if char == 'a' or char == 'e' or char == 'i' \
           or char == 'o' or char == 'u':
            numVowels += 1
        elif char == 'o' or char == 'M':
            print char
        else:
            numCons += 1

    print 'numVowels is: ' + str(numVowels)
    print 'numCons is: ' + str(numCons)
    return numVowels, numCons

def wordcount(s):
    numWords=0
    w=s.split()
    
    print w
    numWords=len(w)
    return numWords
    
s="Massachusetts Institute of Technology"

v,c = charcount(s)
print "Number of Vowels are " +str(v)+" Number of Vowels are " + str(c)

n= wordcount(s)
print "Number of Words are " +str(n)
