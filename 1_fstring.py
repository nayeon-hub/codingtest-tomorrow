age = '10'
name = 'parknayeon'
print('제 나이는',age,'입니다.')
print('제 나이는 {} 입니다.'.format(age))
print(f'제 나이는 {age} 입니다. 제 이름은 {name} 입니다.')

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')

import datetime

date= datetime.datetime.now()
print(f'{date:%Y-%m-%d-%A}')