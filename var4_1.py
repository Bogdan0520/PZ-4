cost = float(input())

if cost < 0:
    raise BaseException(f'Число должно быть положительным! Вы ввели {cost}')

for mass in range(11):
    print(mass / 10 * cost, end=' ')
    
# cost = -10; BaseException: Число должно быть положительным! Вы ввели -10
# cost = 15; 0.0 1.5 3.0 4.5 6.0 7.5 9.0 10.5 12.0 13.5 15.0 
# cost = 146; 0.0 14.600000000000001 29.200000000000003 43.8 58.400000000000006 73.0 87.6 102.19999999999999 116.80000000000001 131.4 146.0 