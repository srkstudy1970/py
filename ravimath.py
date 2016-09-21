##### To Import Packages########
import math
import os
import random


##### End of Packages#########

##### Welcom Message#########
print "Welcome to Ravi's Math programs"
##### End of Welcome Messages #########



frect_area = 0
frect_perimeter=0

def conv_milestofeet(x):
    feet=5280*float(x)
    print x +" miles is equal to "+ str(feet) +" feet"
    return feet
def conv_feettomiles(x):
    miles=float(x)/5280
    print x +" feet is equal to "+ str(miles) +" miles"
    return miles
def conv_milestokm(x):
    km =float(x)/0.621371
    print x +" miles is equal to "+ str(km) +" Km"
    return km
def conv_kmtomiles(x):
    miles = float(x) *0.621371
    print x +" Km is equal to "+ str(miles) +" miles"
    return miles
    
def conv_hrsminsectosec(x,y,z):
    hrstosec= float(x) * 3600
    minstosec= float(y) * 60
    totalsec=hrstosec+minstosec+float(z)
    print x +" Hrs "+ y + " mins "+ z + " sec " + " is equal to " +str(totalsec)+" seconds"
    return totalsec
def conv_secondstohrsminsec(x):
    hrs=float(x)/3600.0
    mins = (float(x) - (int((hrs))*3600))/60.0
    sec = mins- int(mins)
    print x + " seconds is equal to " +str(int(round(hrs)))+" hrs "+ str(int((mins))) + " mins "+ str(int(round((sec)*60.0))) + " secs"
    return hrs
def conv_inchestocm(x):
    cm=float(x)*2.54
    print x +" inches is equal to " + str(cm)+" cm"
    return cm
def conv_ftok(fahrenheit):
    kelvin = (5.0 / 9) * (float(fahrenheit) - 32)
    print "The Fahrenheit " +str(fahrenheit)+" in Kelvin is "+ str(kelvin) + " K"
    return kelvin

def conv_cmtoinches(x):
    inches=float(x)/2.54
    print x +" centimeter is equal to " + str(inches)+" inches"
    return inches

##################### Geometrical Shapes functions ##############################

def rect_area(x,y):
    rectarea = float(x) * float(y)
    # I am experiementing with  globalvariables,the idea is to count the number of times
    # this function has been called during a program execution, hence increamenting the frect_area variable by 1 each time
    # this function is called
    global frect_area
    frect_area = frect_area+1
    print "The Area of Rectangle is : " + str(area) +" sqcm"
    return rectarea

def rect_perimeter(x,y):
    rectperimeter = 2*(float(x) + float(y))
    global frect_perimeter
    frect_perimeter = frect_perimeter+1
    print "The Perimeter of Rectangle is : " + str(p) +" cm"
    return rectperimeter
def circle_area(r):
    circlearea= 2* math.pi * float(r) **2
    print "Area of a circle with a given radius of "+ str(r)+ " is "+ str(area)+ " sqcm"
    return circlearea
def circle_circum(r):
    circlecircum = 2*math.pi*float(r)
    print "Circumference of a circle with a given radius of "+ str(r)+ " is "+ str(circum)
    return circlecircum

def tri_areaH(s1,s2,s3):
    # this is calculated as per Heron's formula for area of a triangle with the length of 3 given sides
    #sp is semi perimeter
    #sp=(float(s1)+float(s2)+float(s3))/2
    s1=float(s1)
    s2=float(s2)
    s3=float(s3)
    sp=(s1+s2+s3)/2
    if sp == s1 or sp == s2 or sp == s3: 
        print "Impossible triangle exiting/returning"
        return "Impossible triangle"
    else:
        '''
        print "all ok"
        print "sp = " + str(sp)
        print "s1 = " + str(s1)
        print "s2 = " + str(s2)
        print "s3 = " + str(s3)
        #print str(float(s1))
        #print str(sp*(sp-float(s1))*(sp-float(s2))*(sp-float(s3)))
        '''    
        triarea=math.sqrt(sp*(sp-s1)*(sp-s2)*(sp-s3))
        print "Area of a triangle with sides "+ str(s1)+ "cm, "+ str(s2)+ "cm, "+str(s3)+"cm is "+ str(format(triarea, '.2f'))+ " sqcm"
        return triarea

def distance_calc(x1,y1,x2,y2):
    x=float(x1)-float(x2)
    y=float(y1)-float(y2)
    
    distance= math.sqrt((x**2)+(y**2))
    print "The distance between ("+str(x1)+","+str(y1)+") and ("+ str(x2)+","+str(y2)+") is "+str(distance)
    return distance

def tri_areawithcoordinates():
    print "To Calculate Area of Triangle using Heron's forumula when the coordinate of the vertices are given"
    try:
        input = raw_input("Enter coordinates of vertices x1,y1,x2,y2,x3,y3 separated by commas: ")

        input_list = input.split(',')
        numbers = [float(x.strip()) for x in input_list]
        print str(numbers)
        print str(len(numbers))
        s1=distance_calc(numbers[0],numbers[1],numbers[2],numbers[3])
        s2=distance_calc(numbers[2],numbers[3],numbers[4],numbers[5])
        s3=distance_calc(numbers[0],numbers[1],numbers[4],numbers[5])
        ta=tri_areaH(s1,s2,s3)
    
    except:
        print "Please enter comma separated numbers"
        print "error "+str(IOError)
    
    finally:
        print "In the finally clause"
        return ta

################################# End of Shapes ##############################

def future_value(p,r,t):
    fv= float(p) *(1+(0.01*float(r)))*float(t)
    print "The future value of amt $"+str(p)+" at a given interest rate of "+str(r)+"%"+'\n'
    print "for a duration of "+str(t)+" years is $"+str(fv)
    return fv
########## Math functions #############
def print_digits(number):
	"""Prints the tens and ones digit of an integer in [0,100)."""
	
	print "The tens digit is " + str(number // 10) + ",",
	print "and the ones digit is " + str(number % 10) + "."
def powerball():
    """Prints Powerball lottery numbers."""
    
    print "Today's numbers are " + str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ". The Powerball number is",
    print str(random.randrange(1, 60)) + "."
def is_even(num):

    print "Inside is even function " + str(num)
    ev = num % 2
    if ev == 0:
        print "This is even number"
    else:
        print "this is odd number"
    return ev
def is_leap_year(year):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))
def testleap(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
        ly= 'True'
        return ly
    else:
        print year, "is not a leap year."
        ly= 'False'
        return ly
########## Math functions #############
'''
rect_area(raw_input("Please Enter Length in cm: "),raw_input("Please Enter Breadth in cm: "))
rect_perimeter(raw_input("Please Enter Length in cm: "),raw_input("Please Enter Breadth in cm: "))
print "Area of rectangle function has been called: "+str(frect_area)+ " times"
print "Perimeter of rectangle function has been called: "+str(frect_perimeter)+ " times"
conv_milestofeet(raw_input("Please Enter Miles to convert into feet: "))
conv_feettomiles(raw_input("Please Enter Feet to convert into Miles: "))
conv_milestokm(raw_input("Please Enter Miles to convert into Km: "))
conv_kmtomiles(raw_input("Please Enter Km to convert into Miles: "))
print "To Convert Hrs, mins and seconds to Seconds:"
conv_hrsminsectosec(raw_input("Please Enter Hrs: "),raw_input("Please Enter Mins: "),raw_input("Please Enter Sec: "))
print "To Convert Seconds to Hrs, Mins, Seconds"
conv_secondstohrsminsec(raw_input("Please Enter Seconds to convert to Hrs Mins and Sec: "))              
print "To convert Inches to Centimeters"
conv_inchestocm(raw_input("Please Enter Inches to convert to Cm: "))
print "To convert Centimeters to Inches"
conv_cmtoinches(raw_input("Please Enter Centimeters to convert to Inches: "))
print "To convert F to K"
conv_ftok(raw_input("Please Enter fahrenheit to Convert to Kelvin: "))

# From here it is Geometry
print "To Calculate the area of a Circle when its radius is given"
circle_area(raw_input("Please Enter radius in cm: "))
print "To Calculate the Circumference of a Circle when its radius is given"
circle_circum(raw_input("Please Enter radius in cm: "))
print "To Calculate the Future value of principle amount when the interest rate and the number of years is given"+'\n'
future_value(raw_input("Please Enter Principle in $: "),raw_input("Please Enter Rate of interest: "),raw_input("Please Enter numer of years: "))

print "When the coordinates are given find the distance between them"+'\n'
distance_calc(raw_input("Please Enter Position of x1: "),raw_input("Please Enter Position of y1: "),raw_input("Please Enter Position of x2: "),raw_input("Please Enter Position of y2: "))


print "When the sides of a triangle are given we can calculate the area using heron's formula"+'\n'
tri_areaH(raw_input("Please Enter length of side a in cm: "),raw_input("Please Enter length of side b in cm: "),raw_input("Please Enter length of side c in cm:: "))



print "To Calculate Area of Triangle using Heron's forumula when the length of the 3 sides is given"
#tri_areaH(10,20,30)
#tri_areaH(1,2,3)
#tri_areaH(4,5,6)
#tri_areaH(4.5,5.5,6.5)
#tri_areaH(4500,5500,6500)

print "To Calculate Area of Triangle using Heron's forumula when the coordinate of the vertices are given"
tri_areawithcoordinates()

print "The below function will split the number and gives the digits in 10's place and 1's place when a 2 digit number is given"
print_digits(98)

print '\n'+ "The Below function will call the random numbers and simulate the powerball lottery"
powerball()
powerball()
powerball()
is_even(7)
'''

t=testleap(1990)
print t
t=testleap(2000)
print t
t=testleap(2002)
print t

