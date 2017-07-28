from datetime import date

d = date(2012, 12, 21)
print(format(d))
# 2012-12-21
print(format(d, '%A, %B %d, %Y'))
# Friday, December 21, 2012
print('The end is {:%d %b %Y}. Goodbye'.format(d))
# The end is 21 Dec 2012. Goodbye
