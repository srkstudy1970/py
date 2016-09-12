#######################- About this Program-##############
# This is......
#1. Packages
#2. Functions
#3. Welcome Menu
#3. Main 
#######################- END -About this Program-##############

#######################- Packages-##############
print "Packages"
import os

import time
from datetime import timedelta

#######################- End of Packages-##############

#######################- Functions-##############
print "Functions"
def fileappend(fname,mdata):
    print "Inside fileappend"
    file = open(fname, "a")
    file.write('\n'+'\n'+'\n'+"Metadata Start" + '\n')
    file.write(mdata)
    file.write('\n'+ "Metadata End")
    file.close()
    print "Exiting Fileappend"


def directory(path,extension):
    '''
    This functions takes the folder name and the file extension and returns the numbder of
    files in the folder which are matching the extension provided
    '''
    #print "Inside directory"
    #print path
    list_dir = []
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        print file
        st = os.stat(path+'/'+file)
        print st.st_size
        if file.endswith(extension): # eg: '.txt'
            count += 1
    return count
    #print "Exit directory"

#######################- End of Functions-##############

#######################- Welcome Menu-##############
print "Menu"
#######################- End of Welcomg Menu-##############

#######################- Main-##############
print "Main"
'''
size = 200
for i in range (1,10):
    mydata ="Size of the File is : " + str(size)
    myfile = "txtfiles\myfile"+str(i)+".txt"
    fileappend(myfile,mydata)
'''
start_time = time.localtime(0)
# do your work here
print type(start_time)
print "Time is : " + str(start_time)


path ="txtfiles"
extension="txt"
total_files =directory(path,extension)
print "Total files in folder " + path + "is: "+ str(total_files)
#######################- End of Main-##############
