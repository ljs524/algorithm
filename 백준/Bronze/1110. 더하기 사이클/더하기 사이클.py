N = int(input())
num = N
cnt = 0

while 1:
    a = num // 10
    b = num % 10
    # a는 10으로 나눈 몫, b는 10으로 나눈 나머지이다. 0 <= N < 99인 값이 주어진다면 무조건 두자리 수니까 몫과 나머지를 10으로 나누면 된다.
    # 나눗셈에 익숙하다보니 몫과 나머지 개념이 아직 익숙하지 않아서 바로 생각이 안 난다.
    c = (a + b) % 10
    # c는 a와 b를 더한 값의 나머지이다.
    num = (b * 10) + c
    # 최종 숫자는 b를 10의 자리에 두고 끝에 c를 더한다.
    cnt += 1
    if(num == N):
        break
    # num에 들어온 값이 N에 들어왔던 값과 동일할 경우, break한다.
print(cnt)