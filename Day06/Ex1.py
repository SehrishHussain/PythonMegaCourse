# Please download the essay.txt file from the resources of this article.
# Then, create a program that reads that file and prints out its text.
# The first letter of each word in the output should be uppercase.

file = open('essay.txt', 'r')
for content in file:
    print(type(content))
    print(content.title())
file.close()
###########################################33
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file = open('essay.txt', 'r')
for content in file:
    print(len(content))
file.close()

######################################################################
# Please download the members.txt file from the resources of this article.
#
# Then, create a program that, whenever executed, asks the user to enter a new member in the command line:
#
# Then, the member is added to members.txt. In this case, the text file content would be:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right

name = input("Add a new  member: ")
file = open('members.txt', 'a+')  # + indicates both read and write
file.write(name + '\n')
file.close()

##############################################################################
# Create a program that generates multiple text files by iterating over the filenames list.
# The text Hello should be written inside each generated text file.

filename = ['one.txt', 'two.txt', 'three.txt', 'four.txt']
for items in filename:
    file = open(items, 'w+')
    file.write("Hello")
file.close()

##################################################################################
# Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file and prints out the content of each in the command line.
# The expected output would be like the following:

files = ['a.txt', 'b.txt', 'c.txt']
for file in files:
    f = open(file, 'r')
    print(f.readline())
f.close()

