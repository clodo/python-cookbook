import io

s = io.StringIO()
s.write('Hello World\n')

print('This is a test', file=s)

# Get all of the data written so far
value = s.getvalue()
print(value)

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

# Binary data
s = io.BytesIO()
s.write(b'binary data')
value = s.getvalue()
print(value)
