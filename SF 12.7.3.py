money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent.values():
    print(key)
    deposit.append(int(key*money/100))
deposit_i = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать", deposit_i)