def countWordsFromFile():
        fileName=input("enter the file name: ")
        file=open(fileName, "r")
        wordCount=0
        for line in file:
                words=line.split()
                print(words)
                wordCount=wordCount+len(words)
                print(wordCount)
        print("Number of words: ")
        print(wordCount)

countWordsFromFile()