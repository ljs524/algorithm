import sys
stack = []

while 1:
    input = sys.stdin.readline().split('\n')[0]
    if input == '문제':
        stack.append(input)
    if input == '고무오리':
        if not stack:
            stack.append('문제')
            stack.append('문제')
        else:
            stack.pop()
    if input == '고무오리 디버깅 끝':
        break

if stack:
    print('힝구')
else:
    print('고무오리야 사랑해')