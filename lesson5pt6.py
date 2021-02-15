subjects = {}
with open('text_6.txt', 'r', encoding = "utf-8") as file:
    for line in file.readlines():
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    print(subjects)
