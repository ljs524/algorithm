alph = input()
cro_alph = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro_alph:
    alph = alph.replace(i, 'a')
    # 리플레이스 함수를 사용하여 임의의 a 값으로 변경한 뒤 계산한다.
print(len(alph))