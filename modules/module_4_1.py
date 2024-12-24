from modules.my_math.fake_math import drive as fake_drive
from modules.my_math.true_math import drive as true_drive

first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

call_1 = fake_drive(first, second)
call_2 = true_drive(first, second)

print(*call_1)
print(*call_2)
