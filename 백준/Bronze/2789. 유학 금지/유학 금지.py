string = input()
result = ''
for s in string:
    if s not in 'CAMBRIDGE':
        result += s
print(result)