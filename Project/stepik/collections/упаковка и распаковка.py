#* упаковка в список/распаковка в кортеж
# ** упаковка в словарь

x, *y = (1, 2, 3, 4)
#x = 1
#y = [1, 2, 3]

*x, y = (1, 2, 3, 4)
#x = [1, 2, 3]
#y = 4

x, *y = [1, 'a', True, 4]
#x = 1
#y = ['a', True, 4]

*x, y, z = 'Hello Python!'
#x = ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o']
#y = 'n'
#z = '!'

a = [1, 2, 3]
b = tuple(a) #(1, 2, 3) =
b = (*a,) #(1, 2, 3)

d = 5, -5 #(-5, 5)
range(*d) #range(5, -5)
[*range(*d)] #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4] = list(range(*d))
[*range(*d), *(True, False), *a] #[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, True, False, 1, 2, 3]

d = {0:'very bad', 1:'bad', 2:'soso', 3:'ok', 4:'good', 5:'very good'}
{*d} #{0, 1, 2, 3, 4, 5} ключи запаковали в кортеж
{*d.keys()} #{0, 1, 2, 3, 4, 5}
{*d.values()} #{'very bad', 'bad', 'soso', 'good', 'very good', 'ok'}
{*d.items()} #{(1, 'bad'), (5, 'very good'), (4, 'good'), (2, 'soso'), (3, 'ok'), (0, 'very bad')}

d2 = {6:'six', 7:'seven'}
{**d, **d2} #{0: 'very bad', 1: 'bad', 2: 'soso', 3: 'ok', 4: 'good', 5: 'very good', 6: 'six', 7: 'seven'} обьединение словарей

