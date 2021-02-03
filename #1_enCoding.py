
# #<문제풀이>
# l = []
# text = ['  + -- + - + -  ',
# '  + --- + - +  ',
# '  + -- + - + -  ',
# '  + - + - + - +  ']
# for i in text:
#     l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))
# print(''.join(l))

# print(''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text]))


# #<내가 푼 방법>
# l = []
# list2 = []
# for i in range(len(text)):
#     b = 6
#     s = 0 
#     y = 0
#     l.append(text[i].strip().replace(' ',''))
#     for j in range(len(l[i])):
#         if l[i][j] == '+':
#            a = 1
#            y = a*2**b
#         elif l[i][j] == '-':
#             a = 0
#             y = a*2**b
# # 직접 2진법을 계산하는 대신에 (int(),2)를 사용함
#         s += y
#         b -= 1
# # for대신에 replace를 사용함 
#     list2.append(chr(s))
# #아스키코드 숫자를 문자로 바꿀 때는 chr()
# print(''.join(list2))

# 예제 구구단
['str(i),'*',str(j),'=',i*j'for i in range(2,10) for j in range(1,10)]

#3.6 Version
