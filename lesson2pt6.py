features = {'название': '', 'цена': '', 'количество': ''}
analytics = {'название': [], 'цена': [], 'количество': []}
num = 1
while True:
    control = input("для выхода '1', для ввода товара 'Enter', для вывода аналитики '2'")
    num += 1
    if control == '1':
        break
    if control == '2':
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features.keys():
        feature_ = input(f'введите "{f}"')
        features[f] = feature_
        analytics[f].append(features[f])


