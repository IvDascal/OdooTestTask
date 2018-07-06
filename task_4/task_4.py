# Завдання 4. 
# Дано товарний чек. В ньому знаходяться товари, кількість та ціна. Підсумок чеку містить розрахунок податку.
# Ваша задача скорелювати розрахунок податку на одну позицію в чеку так,
# щоб в підсумок податків на кожну позицію дорівнював загальному підсумку. Точність виведення два знаки після коми.

# Задача сформувати розрахунок стовпчика “податок на позицію” так щоб в підсумку виходила сума 1434.07,
# при цьому точність має бути два знаки. Дозволено додавати,
# віднімати необхідну кількість але потрібно обирати найближче із значень.

from functools import reduce

tax_percentage = 20
tax_sum = 1434.07

items = [
    (397.01, 1), 
    (435.0, 2), 
    (435.0, 2), 
    (443.33, 2), 
    (443.33, 2), 
    (370.0, 2), 
    (630, 1), 
    (630, 1), 
    (630.0, 2)
]

items_sum = [x*y for x, y in items]

invoice_sum = (reduce(lambda x, y: x+y, items_sum))

tax_delta = round(tax_sum - invoice_sum*(tax_percentage/100), 3)

items_tax = list(map(lambda x: x * (tax_percentage/100), items_sum))

tax_calculated = reduce(lambda x, y: x+y, items_tax)

tax_rounded_inx = []
for inx, elem in enumerate(items_tax):
    if elem != round(elem, 2):
        tax_delta += (elem - round(elem, 2))
        tax_delta = round(tax_delta, 3)
        items_tax[inx] = round(elem, 2)
        tax_rounded_inx.append(inx)

for inx in tax_rounded_inx:
    if tax_delta >= 0.01:
        items_tax[inx] = round((items_tax[inx] + 0.01), 2)
        tax_delta -= 0.01

        check_tax_sum = round(reduce(lambda x, y: x+y, items_tax), 2)
        if tax_sum == check_tax_sum:
            continue

for elem in items_tax:
    print(elem)
