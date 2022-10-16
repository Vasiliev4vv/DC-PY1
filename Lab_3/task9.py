salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
increase_coeff = increase + 1 # коэффициент роста цен
# Будем считать, что сначала происходит начисление зарплаты, а уже после - траты.
need_money = 0  # количество денег, чтобы прожить 10 месяцев
for i in range(1,11):
    need_money += spend - salary
    spend *= increase_coeff
# TODO Оформить решение

print(round(need_money))
