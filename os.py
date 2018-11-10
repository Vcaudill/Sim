
import os

print(os.getcwd())
# os.getcwd() prints working directory
# To print absolute path on your system
# os.path.abspath('.')

# To print files and directories in the current directory
# on your system
# os.listdir('.')

try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:

    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)

# In any case, the code then continues with
# the line after the try/except

fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.
'''
os.close(): Close file descriptor fd. A file opened using open(), can be closed
by close()only. But file opened through os.popen(), can be closed with close()
or os.close(). If we try closing a file opened with open(), using os.close(),
Python would throw TypeError.
'''
os.rename(fd, 'New.txt')  # this will rename a file soo coool

mypath = path = "/Users/victoria/Desktop/Sim/newfoldertest"
if not os.path.isdir(mypath):
    os.makedirs(mypath)  # this creates a new folder puuuurrrrfict
