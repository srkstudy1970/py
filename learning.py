def rangeex1():
    num = 0
    for num in range(5):
        print num
    print num
    print "End of rangeex1"

def rangeex2():
    divisor = 2
    for num in range(0, 10, 2):
        print num/divisor
    print "End of rangeex2"

def rangeex3():
    for variable in range(20):
        if variable % 4 == 0:
            print variable
        if variable % 16 == 0:
            print 'Foo!' 
    print "End of rangeex3"
def rangeex4():
   
    for num in range(2, 12, 2):
        print num
    print "GoodBye!"
    print "End of rangeex4"
def rangeex5():
    print "Hello!"
    for num in range(12, 2, -2):
        print num
    print "GoodBye!"
    print "End of rangeex5"
    
def infunc1():
    for letter in 'hola':
        print letter
    print "End of infunc"
def infunc2():
    count = 0
    for letter in 'Snow!':
        print 'Letter # ' + str(count) + ' is ' + str(letter)
        count += 1
        #break
    print count 
    print "End of infunc2"
def forex1():
    end=8
    s=0
    for i in range(1,end+1):
        s=s+i
    print s

def myitr1():
    iteration = 0
    count = 0
    while iteration < 5:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        iteration += 1 
def myitr2():
    iteration = 0
    
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        iteration += 1 
def myitr3():
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
            if iteration % 2 == 0:
                break
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        iteration += 1 

def convertb2d():
    b=str(010010)
    print len(b)
    count = 0
    cd=0
    for i in b:
        cd = (cd * 2) + int(i)
        print "The number in position # " +str(count)+ " is "+ i + " the current digit is " + str(cd)
        count =count + 1
    print str(cd)
'''    
#rangeex1()
#rangeex2()
#rangeex3()
rangeex5()
infunc1()
infunc2()
forex1()
myitr1()
myitr2()
myitr3()
'''
convertb2d()
