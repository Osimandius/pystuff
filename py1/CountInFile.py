def countFromFile():
    fileName=input("Give the .txt file to be counted")
    numberWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberWords=numberWords+len(words)
    print(str(numberWords+" words are in the file."))

countFromFile()