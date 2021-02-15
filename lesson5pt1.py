with open("text_1.txt", 'w', encoding='utf-8') as file:
    while True:
        user_input = input('Введите произвольную строку: ')
        if not user_input:
            break
        file.write(f'{user_input}\n')
