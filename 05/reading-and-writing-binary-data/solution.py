# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# Read the entire file as a sinble byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()
    print(data)

# Read or write text from a binary-mode file
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
