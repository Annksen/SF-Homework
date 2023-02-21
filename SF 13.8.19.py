number_of_ticket = int(input('Введите количество билетов:'))
age = [int(input('Введите возраст посетителя: \n')) for i in range(number_of_ticket)]
cost = 0

for i in age:
    if i < 18:
        cost += 0
    if 17 < i < 25:
        cost += 990
    if i >= 25:
        cost += 1390

if number_of_ticket >= 3:
    final_cost = cost * 0.9
else:
    final_cost = cost

print(final_cost)
