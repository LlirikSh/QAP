money = int(input("Введите сумму которую планируете положить под проценты: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(int(per_cent[key] * money / 100))
max_summa = int(max(deposit))
print(deposit)
print ("Максимальная прибыль которую вы можете получить — " + str(max_summa))
