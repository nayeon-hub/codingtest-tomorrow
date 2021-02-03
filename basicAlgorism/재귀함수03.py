##문제 접근 방법

#1. 반복문의 경우는 bottom-up(작은문제에서 출발)
#2. 재귀의 경우는 Top-down(큰 문제에서 출발)
# 꼭 종료조건이 있어야 한다. 안그러면 무한 반복

#반복문 - 합
x = 0
for i in range(11):
    x+=i
print(x)

#재귀함수 - 합
def f(n):
    if n <= 1:
        return 1 #종료조건
    else:
        return n + f(n-1)
print(f(10))

#while문 - 무한루프
# while True:
#     if input('##') == 'exit':
#         break
#     if input('##') == 'hi':
#         print('hello world')
#     else:
#         continue

#재귀함수 - 무한루프
# def console():
#     if input('##') == 'exit':
#         return None
#     if input('##') == 'hi':
#         print('hello world')
#     console()
# console()

#반복문 - 2진수 구하기
print(bin(11))
print(oct(11))
print(hex(11))