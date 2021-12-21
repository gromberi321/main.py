from random import randint
def input(a):
    for i in range (len(a)):
        for j in range (len(a[i])):
            a[i][j] = randint(-40, 60)
arr = [[randint(-40, 60) for i in range(6)] for j in range(6)]
input(arr)
for i in arr:
    print(*i, sep='\t\t')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if int(arr[i][j]) < 0 and int(arr[i][j])%2!=0:
            B = arr[i][j]
            print(f'B: ', format(B))
print()
print('Программу выполнил студент ФГиИб ИСиТ 1-1Б Арвентий Михаил')