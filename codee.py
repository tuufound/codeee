num = int(input())
a = num // 1000   #первая
b = (num % 1000 ) //100   #вторая
c = (num % 100) // 10   #третья
d = (num % 10) #четвертая
#print(a, b, c, d)
sum = a + d
div = b - c
if sum == div:
    print('ДА')
else:
    print('НЕТ')





#print('ДА')

#print('НЕТ')