# Du skal lave et program, der tæller, hvor mange gange hvert ord optræder i en tekst.

# Brugeren indtaster en tekst
# Programmet tæller hvert ords forekomst

# lower() er jeres ven og split() Python String split() MethodLinks til en ekstern webside.

# Eksempel:
    
# Input: "kat hund kat fugl hund kat"
# Output: kat: 3 hund: 2 fugl: 1

# Blank dict to add words with values to
wordList = {}

# What the user needs to do and a input function to store their input in
print("Here you can either type a text or incert a text to find out how many times each word is used in the text")
text = input("").lower()

# this splits the text and adds all the words into a list
words = text.split()

# loop for going through the split up words adding words to a dict and a value of how many times its in the text
for word in words:
    if word in wordList:
        wordList[word] += 1 
    elif word not in wordList:
        wordList[word] = 1
    
        
# Printing the list with the value of how many times its in the text
print(wordList)
