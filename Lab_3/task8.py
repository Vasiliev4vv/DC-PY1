money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
increase_coeff = increase + 1 # коэффициент для умножения
month = 0  # количество месяцев, которое можно прожить
# будем считать, что расходы могут подождать до прихода зарплаты.
# тогда можем посчитать траты с учётом
while (money_capital > 0):
    money_capital += salary - spend
    spend *= increase_coeff
    if money_capital > 0:
        month += 1

# TODO Оформить решение

print(month)
