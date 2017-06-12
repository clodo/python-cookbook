# If the file does not exist create it, otherwise it overwrites the file
with open('somefile.txt', 'wt') as f:
    f.write('Hello\n')


# If the file exists it throws FileExistsError, otherwise the file is created
with open('somefile.txt', 'xt') as f:
    f.write('Hello\n')
