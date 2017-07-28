_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2017, 7, 28)
print(format(d))
# 2017-7-28
print(format(d, 'mdy'))
# 28/7/2017
print('The date is {:ymd}'.format(d))
# The date is 2017-7-28
print('The date is {:mdy}'.format(d))
# The date is 28/7/2017
