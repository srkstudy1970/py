##### To Import Packages########
import math

##### End of Packages#########


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

def rect_area(x,y):
    area = float(x) * float(y)
    # I am experiementing with  globalvariables,the idea is to count the number of times
    # this function has been called during a program execution, hence increamenting the frect_area variable by 1 each time
    # this function is called
    global frect_area
    frect_area = frect_area+1
    print "The Area of Rectangle is : " + str(area) +" sqcm"
    return area

def rect_perimeter(x,y):
    p = 2*(float(x) + float(y))
    global frect_perimeter
    frect_perimeter = frect_perimeter+1
    print "The Perimeter of Rectangle is : " + str(p) +" cm"
    return p
def circle_area(r):
    area= 2* math.pi * float(r) **2
    print "Area of a circle with a given radius of "+ str(r)+ " is "+ str(area)
    return area
def circle_circum(r):
    circum = 2*math.pi*float(r)
    print "Circumference of a circle with a given radius of "+ str(r)+ " is "+ str(circum)
    return circum
def future_value(p,r,t):
    fv= float(p) *(1+(0.01*float(r)))*float(t)
    print "The future value of amt $"+str(p)+" at a given interest rate of "+str(r)+"%"+'\n'
    print "for a duration of "+str(t)+" years is $"+str(fv)
    return fv

def distance_calc(x1,y1,x2,y2):
    x=float(x1)-float(x2)
    y=float(y1)-float(y2)
    
    distance= math.sqrt((x**2)+(y**2))
    print "The distance between ("+str(x1)+","+str(y1)+") and ("+ str(x2)+","+str(y2)+") is "+str(distance)
    return distance

def tri_areaheron(x,y,z):
    #calc s=half of (x+y+z)
    s= 0.5(x+y+z)
    tarea = math.sqrt(s*(s-x)*(s-y)*(s-z))
    print "the area of a triangle with sides "+ str(x)+" " +str(y)+ " " + str(z)+ " is " + str(tarea)+ " sqcm"
    return tarea


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
print "To Calculate the area of a Circle when its radius is given"
circle_area(raw_input("Please Enter radius in cm: "))
print "To Calculate the Circumference of a Circle when its radius is given"
circle_circum(raw_input("Please Enter radius in cm: "))
print "To Calculate the Future value of principle amount when the interest rate and the number of years is given"+'\n'
future_value(raw_input("Please Enter Principle in $: "),raw_input("Please Enter Rate of interest: "),raw_input("Please Enter numer of years: "))

# This is Geometry
print "When the coordinates are given find the distance between them"+'\n'
distance_calc(raw_input("Please Enter Position of x1: "),raw_input("Please Enter Position of y1: "),raw_input("Please Enter Position of x2: "),raw_input("Please Enter Position of y2: "))


print "When the sides of a triangle are given we can calculate the area using heron's formula"+'\n'
tri_areaheron(raw_input("Please Enter lenght of side a in cm: "),raw_input("Please Enter lenght of side b in cm: "),raw_input("Please Enter Plenght of side c in cm:: "))
'''

print "To convert F to K"
conv_ftok(raw_input("Please Enter fahrenheit to Cconvert to Kelvin: "))
