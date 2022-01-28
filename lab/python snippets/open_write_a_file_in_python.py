# https://www.w3schools.com/python/python_file_write.asp

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
