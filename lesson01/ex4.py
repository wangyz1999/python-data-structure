import sys

f = open(sys.argv[2],'r')

line = f.readline()

while(line != ''):
    if(line.find(sys.argv[1]) > -1):
        print(line, end = '')
    line = f.readline()

f.close()
