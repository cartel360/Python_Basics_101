# Open a file
"""
fo = open("sample.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()


# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)
# Close opened file
fo.close()


import os
# Rename a file from foo.txt to test2.txt
os.rename( "foo.txt", "test2.txt" )
"""

import os
# Delete file test2.txt
os.remove("test2.txt")