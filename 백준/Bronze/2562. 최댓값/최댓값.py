n_list = []

for n in range(9):
    n_list.append(int(input()))
print(max(n_list))
print(n_list.index(max(n_list))+1)