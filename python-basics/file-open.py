# A file object can be created ("opened") for reading ("r" mode), for writing ("w" 
# mode), or for appending ("a" mode) to a file.

outfile = open('tmp.txt', 'w') # create file and add content
outfile.write('This is line #1\n')
outfile.write('This is e #2\n')
outfile.write('This is line #3\n')
outfile.close()

outfile = open('tmp.txt', 'a')
outfile.write('Line # 4\n')


infile = open('tmp.txt', 'r')
content = infile.read()
print (content)

