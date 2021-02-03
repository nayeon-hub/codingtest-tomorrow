#1부터 n까지의 합과 곱
# 반복문<->재귀함수

#합
#시그마 공식 n*(n+1)//2 (//는 정수 나누기 연산자)
s = 0
n = int(input())
for i in range(1,n+1):
    s += i
print(s)

z =  n*(n+1)//2
print(z)

#곱
#팩토리얼
# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
s = 1
n = int(input())
for i in range(1,n+1):
    s *= i
print(s)