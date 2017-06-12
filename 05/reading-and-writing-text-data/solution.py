# Read the entire file as a single string
with open('tarumba.doc', 'rt') as f:
    data = f.read()
    print(data)

# Iterate over the lines of the file
with open('tarumba.doc', 'rt') as f:
    for line in f:
        print(line)

# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write("Some line")
    f.write("Another line")

# Redirect print statement
with open('someotherfile.txt', 'wt') as f:
    print("Some line", file=f)
    print("Another line", file=f)

# Append text to the end of an existing file
with open('someotherfile.txt', 'at') as f:
    print("Last line", file=f)

# Define encoding
with open('someotherfile.txt', 'rt', encoding='latin-1') as f:
    print(f.read())
