from sys import argv

lines, words, characters = 0,0,0
with open(argv[1],'r') as f:
    for line in f:
         lines += 1
         characters += len(line)
         words += len(line.split())
    print("{} {} {} {}".format(lines, words, characters, argv[1]))
