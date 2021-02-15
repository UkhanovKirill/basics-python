rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding = "utf-8") as file_eng:
    for i in file_eng:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + i[1])
    print(new_file)
with open('text_new.txt', 'w', encoding = "utf-8") as file_2:
    file_2.writelines(new_file)