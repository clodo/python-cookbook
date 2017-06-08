import os

# Write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
print(os.listdir('.'))

# Directory listing (raw)
print(os.listdir(b'.'))

# Open file with raw filename
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())
