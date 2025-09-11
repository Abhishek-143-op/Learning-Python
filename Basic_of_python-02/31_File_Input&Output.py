
#Files from here are in the folder named Basic_of_python-02\random folder-for_files/
#1.data.txt      2.output.txt


"""
File I/O: It means opening and closing of the files for reading and writing data in the computer memory .


Basic syntax :          file = open('filename.txt', 'mode')


--------Basic modes of the File I/O---------------------
| Mode   | Purpose                                  |
| ------ | ---------------------------------------- |
| 'r'    | Read (default mode)                      |
| 'w'    | Write (creates a new file or overwrites) |
| 'a'    | Append (adds to the end of file)         |
| 'rb'   | Read in binary mode                      |
| 'wb'   | Write in binary mode                     |
| 'r+'   | Read & write                             |


NOTE: Using w (write mode) will erase the data in the file if file already exists.

"""

"""
Reading Files:

                .read(): Reads entire file as a string.
                .readline(): Reads one line at a time.
                .readlines(): Reads all lines into a list.
"""
file = open('Basic_of_python-02/random folder-for_files/data.txt', 'r')  #If file exists it will open the file in read mode 
content = file.read()#It reads the content of the files.
print(content) #It will print the content of the file.
file.close() #It will close the opened file manually (explicitly.)

#NOTE: If file do not exist it will give an error showing no such file found.



"""
Writing Files : 

                .write(): Writes a string into a file.
"""
file = open('Basic_of_python-02/random folder-for_files/output.txt', 'w')
file.write('Hello, this is a sample text.')
file.close()


"""
Appending Data : It means adding the data at last of the file .

                file= open('file/Folder path', 'a')  Here a means appending the data 

        -------  Use 'a' to add data without deleting existing content.
"""
file = open('Basic_of_python-02/random folder-for_files/output.txt', 'a')
file.write('\nThis line is appended.')
file.close()


#********************************************IMP********************************************************************
"""
Best Practice: Using with Statement

            Automatically handles closing the file:
"""
with open('Basic_of_python-02/random folder-for_files/data.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to call file.close()

#********************************************************************************************************************

#Do this for later on -----------------------------------------;;;;;;

'''
"""
Handling large files: 
            Avoid .read() for large files (may crash your program).

            use a loop with .readline() or iterate the file object:

"""

with open('Basic_of_python-02/random folder-for_files/largefile.txt', 'r') as file:
    for line in file:
        print(line.strip())   # Simple, correct

        '''