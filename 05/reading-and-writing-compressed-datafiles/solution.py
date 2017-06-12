import gzip
import bz2

# Writing gzip file
with gzip.open('somefile.gz', 'wt') as f:
    f.write('Some text')

# Writing bz2 file
with bz2.open('somefile.bz2', 'wt') as f:
    f.write('Some text')

# Reading gzip file
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
    print(text)

# Reading bz2 file
with bz2.open('somefile.bz2', 'rt', compresslevel=9) as f:
    text = f.read()
    print(text)
