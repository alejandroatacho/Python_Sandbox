import os

#path = "C:\\Users\\alex_\\Documents\GitHub\\Python_Sandbox\\Main\\file\\placeholder\\test.txt"
# path = "main\\file\\placeholder\\test.txt"  # better version
path = "main//file//placeholder//test.txt"  # Cleaner version
if os.path.exists(path):
    print("that location exists!")
elif os.path.isdir(path):
    print("That is a directory")
else:
    print("that location does not exist")
