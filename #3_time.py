people = 14000605
month = [2**10,2**9,2**8,2**7,2**6,2**5,2**4,2**3,2**2,2**1]
year = 0

while True:
    for i in range(0,10):#달마다
        for k in (1,month[i]+1):
            for j in range(9*60,21*60,10): #9시부터 21시까지 10분씩
                if people <= 0:
                    print(f'{year}년 {11-i}월 {k}일 {j//60}시 {j%60}분')
                    break
                else : 
                    if (j%60 == 0):
                        people -= 25
                    else:
                        people -= 15
    year += 1
