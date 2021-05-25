cointroString=input("enter string: ")
charecterCount=0
wordCount=0
for i in introString:
    charecterCount+=1
    if(i == ' '):
        wordCount+=1
print("number of charecters: ")
print(charecterCount)
print("number of words:")
print(wordCount + 1)