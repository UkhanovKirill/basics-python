from json import dumps
results = [{}, {}]
with open('text_7.txt', 'r', encoding = "utf-8") as fhs:
    lines = fhs.readlines()
for line in lines:
    name, own, proceeds, expenses = line.split()
    results[0][name] = int(proceeds) - int(expenses)
    results[1]['average_profit'] = round(sum(profit for own, profit in results[0].items() if profit > 0) / len(results[0]))
with open('text_77.txt', 'w', encoding = "utf-8") as fhd:
    fhd.write(dumps(results))
