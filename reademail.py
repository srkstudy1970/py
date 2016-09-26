file = raw_input('Enter file name: ')
if len(file) < 1 : file = 'mbox-short.txt'
    
try :
    type(file)
    fhand = open(file)
except :
    print 'Cannot open file:' , file , '.' , '...please try, again.'
    exit()

email_adrs = dict()

for line in fhand :
    if not line.startswith('From ') : continue
    words = line.split()
    email_adrs[words[1]] = email_adrs.get(words[1], 0) + 1

print email_adrs
