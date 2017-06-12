print('ACME', 50, 91.5)
# ACME 50 91.5
print('ACME', 50, 91.5, sep=',')
# ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n')
# ACME,50,91.5!!

for i in range(5):
    print(i, end=' ')
# 0 1 2 3

row = ('ACME', 50, 91.5)
print(*row, sep=',')
# ACME,50,91.5
