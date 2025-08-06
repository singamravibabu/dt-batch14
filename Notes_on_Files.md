# WORKING WITH FILES
##### Two types of files:
1. Text files
2. Binary files

### Text files
- A file with characters and lines is called a text file.
- Each line ends with new line (\n) character.
- Some lines end with \r and \n.
- Examples:
    .txt
    .html
    .xml
    .json
    .csv
    .css

### Binary files
- A binary is a sequence of bytes. It may contain some parts as characters.
- Any non-text file is a binary file.
- Examples:
    - image files
    - database files
    - compressed files
    - video files
    - audio files
    - executable files

### Text files (revisited)
##### File operations
1. Open a file
2. Read from a file or write to a file
3. Close the file

##### Open a file
- The built-in function open() is used to open a file
Syntax:
`open(filename, mode)`
```
> The open() function creates a `file_object`

filename - file name or complete path of the file
mode - There are three modes:
    - r (read)
        - if the file doesn't exists, it throws file not found error.
    - w (write)
        - if the doesn't exists it creates one, if the file already exists then it deletes the existing data from it.
    - a (append)
        - if the doesn't exist it creates one, if the file exists then it appends the new data to the file
    - b (binary)
        We can read binary files using 'rb'
        We can write to binary files using 'wb'


#### Closing a file automatically using 'with' clause
```
with open(filename, mode) as f:
    block
'''
When the block ends the file close automatically, and its all the memory related to the file.


#### Reading files
- read() method
    - it reads all the content (all lines) of the file as one single string
- readlines() method
    - reads all the lines of a file into a list, where each item in the list is a line from the file.
- readline() method
    - reads the next line

#### The write() method
```
write(str)
```
Writes string to a file.