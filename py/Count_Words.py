string=input("Give an intro, midtro, and outro")
print(string)
charCount=0
wordCount=1
for char in string:
    charCount+=1
    if(char==" "):
        wordCount+=1
print("# of characters")
print(charCount)
print("# of words")
print(wordCount)
print("\n\nThanks for playing, Now go away!")