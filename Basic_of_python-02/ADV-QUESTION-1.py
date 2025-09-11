#       ADVANCED QUESTION  1.   --------------        Question practice on File I/O 

'''
 Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.


note : Here this question we already created file named poems.txt then we need to read this file and apply 
respected operation

'''
with open('Basic_of_python-02/random folder-for_files\poem.txt','r') as file :
    #Reading the content of file 
    content = file.read().lower()
    print("Data contained in file Poem.txt: \n",content)

    #Asking the word no. of times appeared in file 
    word=input("Enter the word you want to search in file : ")

#checking wether file contain the specified word in it 
    if word in content:
        print(f"File poem contain {word} word in it \n ")

        #checking how many time the specified word in the file 
        words=content.split()               #spliting lines into the words
        numoftimeword = words.count(word)   #Counting the words in the file.

        print(f"The no. of times {word} appear in the file is : {numoftimeword}")
    else :
        print(f"File poem donot contain {word} word in it ")



