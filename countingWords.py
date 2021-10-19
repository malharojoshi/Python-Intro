introstring=input("enter string: ")
charecterCount=0
wordCount=1
for i in introstring:
    charecterCount=charecterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("number of words in the string")
print(wordCount)
print("number of charecters in the string")
print(charecterCount)